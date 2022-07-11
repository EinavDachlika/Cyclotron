from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error

##table code
#https://pythonguides.com/python-tkinter-table-tutorial/

root = Tk()
#root.geometry("300x300")


root.title("Settings")

#defult font
root.option_add("*Font", "Helvetica")

# connect to MySqL
try:

  db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cyclotron2022@?%",
    database= "cyclotron")

  if db.is_connected():
        # db_Info = db.get_server_info()
        # print("Connected to MySQL Server version ", db_Info)
        dbCursor = db.cursor(buffered=True)
        # dbCursor.execute("select database();")
        # record = dbCursor.fetchone()
        # print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
##################### toolbar #####################

toolbarbgcolor = "white"
toolbar = Frame(root, bg=toolbarbgcolor)
toolbar.grid(sticky='nesw')

# add logo - toolbar
LogoImagePath = Image.open("LogoImage.png")
LogoImageResize = LogoImagePath.resize((120, 57),Image.ANTIALIAS)
LogoImage = ImageTk.PhotoImage(LogoImageResize)
Label(toolbar,image=LogoImage).pack(side=LEFT,padx=10,pady=6)

# work plan button - toolbar
workPlanButton = Button(toolbar, text="Work Plans",font='Helvetica 11')
workPlanButton.pack(side=LEFT,padx=10,pady=3)


# Hospitals button - toolbar
hospitalsButton = Button (toolbar, text="Hospitals",font='Helvetica 11', activebackground='gray')
hospitalsButton.pack(side=LEFT,padx=10,pady=3)

# Orders button - toolbar
ordersButton = Button (toolbar, text="Orders", font='Helvetica 11')
ordersButton.pack(side=LEFT,padx=10,pady=3)


# Reports button - toolbar
reportsButton = Button (toolbar, text="Reports", font='Helvetica 11')
reportsButton.pack(side=LEFT,padx=10,pady=3)

# settings Icon - toolbar

settingsIcon = Image.open("gearIcon.png")
resizedSettingsIcon = settingsIcon.resize((35,35), Image.ANTIALIAS)
imgSettings = ImageTk.PhotoImage(resizedSettingsIcon)
Button(toolbar, image=imgSettings, borderwidth=0).pack(side=RIGHT,padx=10,pady=3)


toolbar.pack(side=TOP, fill=X)

toolbar.grid_columnconfigure(1, weight=1)
##################### ######## #####################

SettingsFrame = Frame(root)
h = Scrollbar(SettingsFrame, orient='horizontal')
SettingsFrame.pack(fill=X)


# feed label
feedLabel = Label(SettingsFrame, text = 'Settings', font=('Helvetica',26, 'bold'),fg='#034672')
PlaceLable_X=50
PlaceLable_Y=10

feedLabel.pack(side=LEFT)
feedLabel.place(x=PlaceLable_X,y=PlaceLable_Y)

##################### Cyclotron #####################
# Cyclotron Details label
CyclotronLabel = Label(SettingsFrame, text = 'Cyclotron Details', font=('Helvetica',15, 'bold'),fg='#034672')
cyclo_Lable_place_x=80
cyclo_Lable_place_y=70

CyclotronLabel.pack(side=LEFT)
CyclotronLabel.place(x=cyclo_Lable_place_x,y=cyclo_Lable_place_y)



# scrollbar
Cyclotron_scroll = Scrollbar(SettingsFrame ,orient="vertical",width=20)
Cyclotron_scroll.pack(side=LEFT)
Cyclotron_scroll.place(x=613, y= 160)

cyclo_list = ttk.Treeview(SettingsFrame, yscrollcommand=Cyclotron_scroll.set,height=5)

cyclo_list.pack(side=LEFT, padx=cyclo_Lable_place_x+30, pady=cyclo_Lable_place_y+50)

# Cyclotron_scroll.config(command=cyclo_list.yview)
# Cyclotron_scroll.config(command=cyclo_list.xview)

# column define

cyclo_list['columns'] = ('Version', 'Capacity (mci/h)', 'Constant Efficiency (mCi/mA)', 'Description')

# column format
width_Version=90
width_Capacity=110
width_Efficiency=185
width_Description=110

cyclo_list.column("#0", width=0, stretch=NO)
cyclo_list.column("Version", anchor=CENTER, width=width_Version)
cyclo_list.column("Capacity (mci/h)", anchor=CENTER, width=width_Capacity)
cyclo_list.column("Constant Efficiency (mCi/mA)", anchor=CENTER, width=width_Efficiency)
cyclo_list.column("Description", anchor=CENTER, width=width_Description)

# Create Headings
cyclo_list.heading("#0", text="", anchor=CENTER)
cyclo_list.heading("Version", text="Version", anchor=CENTER)
cyclo_list.heading("Capacity (mci/h)", text="Capacity (mci/h)", anchor=CENTER)
cyclo_list.heading("Constant Efficiency (mCi/mA)", text="Constant Efficiency (mCi/mA)", anchor=CENTER)
cyclo_list.heading("Description", text="Description", anchor=CENTER)

# add data from db
cursor = db.cursor()
cursor.execute("SELECT * FROM resourcecyclotron")
cyclotrons = cursor.fetchall()

iid=0
for cyclo in cyclotrons:
    print(cyclo)
    cyclo_list.insert(parent='', index='end', iid=iid, text='',
               values=(cyclo[1], cyclo[2], cyclo[3],cyclo[4]))
    iid +=1

cyclo_list.pack()

# frame = Frame(root)
# frame.pack()

get_version=""
get_capacity=""
get_efficiency=""
get_description=""

class Cyclotron:
   def _init_(self,version,capacity,constant_efficiency,description ):
      self.version=version
      self.capacity = capacity
      self.constant_efficiency= constant_efficiency
      self.description=description

   # def edit(self):
   #    def update_record(get_version, get_capacity, get_efficiency, get_description):
   #       selected = cyclo_list.focus()
   #       # save new data
   #       print("get_version" + get_version)
   #       cyclo_list.item(selected, text="", values=(get_version, get_capacity, get_efficiency, get_description))
   #
   #       # # clear entry boxes
   #       # Version_entry.delete(0, END)
   #       # Capacity_entry.delete(0, END)
   #       # Efficiency_entry.delete(0, END)


def open_popup_cyclotron():
   edit_popup= Toplevel(root)
   edit_popup.geometry("900x400")
   edit_popup.title("Edit Cyclotron Details")
   Label(edit_popup, text= "Edit Cyclotron Details", font=('Helvetica 17 bold'), fg='#034672').place(x=10,y=18)

   # labels
   popup_label_y=80
   Version = Label(edit_popup, text="Version")
   Version.grid(row=1, column=1)
   version_x = 20
   Version.place(x=version_x, y=popup_label_y)


   Capacity = Label(edit_popup, text="Capacity")
   Capacity_units = Label(edit_popup, text="(mci/h)")
   Capacity_units.config(font=("Courier", 9))
   Capacity.grid(row=1, column=2)
   capacity_x = version_x+Version.winfo_reqwidth()+70
   Capacity.place(x=capacity_x, y=popup_label_y)
   capacity_units_x=capacity_x + Capacity.winfo_reqwidth()
   Capacity_units.place(x=capacity_units_x, y=popup_label_y+7)


   Efficiency = Label(edit_popup, text="Constant Efficiency")
   Efficiency_units = Label(edit_popup, text="(mCi/mA)")
   Efficiency_units.config(font=("Courier", 9))
   Efficiency.grid(row=1, column=3)
   efficiency_x = capacity_units_x + Capacity_units.winfo_reqwidth() + 50
   Efficiency.place(x=efficiency_x, y=popup_label_y)
   efficiency_units_x=efficiency_x + Efficiency.winfo_reqwidth()
   Efficiency_units.place(x=efficiency_units_x, y=popup_label_y+7)


   Description = Label(edit_popup, text="Description")
   Description.grid(row=1, column=3)
   description_x = efficiency_units_x+ Efficiency_units.winfo_reqwidth() + 30
   Description.place(x=description_x, y=popup_label_y)

   # Entry boxes
   Version_entry = Entry(edit_popup, width=10)
   Version_entry.grid(row=2, column=1)
   Version_entry.place(x=version_x+3, y=popup_label_y+30)

   Capacity_entry = Entry(edit_popup, width=14)
   Capacity_entry.grid(row=2, column=2)
   Capacity_entry.place(x=capacity_x, y=popup_label_y+30)


   Efficiency_entry = Entry(edit_popup, width=15)
   Efficiency_entry.grid(row=2, column=3)
   Efficiency_entry.place(x=efficiency_x, y=popup_label_y+30)


   Description_entry = Entry(edit_popup,width=15)
   Description_entry.grid(row=2, column=4)
   Description_entry.place(x=description_x, y=popup_label_y+30)


   # # clear entry boxes
   # Version_entry.delete(0, END)
   # Capacity_entry.delete(0, END)
   # Efficiency_entry.delete(0, END)

   # grab record
   selected = cyclo_list.focus()
   # grab record values
   values = cyclo_list.item(selected, 'values')
   # temp_label.config(text=selected)

   # insert cyclotron details from db to entry boxes
   Version_entry.insert(0, values[0])
   Capacity_entry.insert(0, values[1])
   Efficiency_entry.insert(0, values[2])
   Description_entry.insert(0,values[3])

   # get_version = Version_entry.get()
   # get_capacity = Capacity_entry.get()
   # get_efficiency = Efficiency_entry.get()
   # get_description = Description_entry.get()

   select_button = Button(edit_popup, text="Save Changes", command=lambda :update_record(Version_entry.get(),Capacity_entry.get(),Efficiency_entry.get(),Description_entry.get()))
   select_button.pack(side=LEFT)
   select_button.place(x=370, y=250)


# in the class?
def update_record(get_version, get_capacity, get_efficiency, get_description):
   print("get_version" + get_version)
   selected = cyclo_list.focus()
   print(cyclo_list.item(selected, 'values'))
   # save new data
   cyclo_list.item(selected, text="", values=(get_version, get_capacity, get_efficiency, get_description))





   # # clear entry boxes
   # Version_entry.delete(0, END)
   # Capacity_entry.delete(0, END)
   # Efficiency_entry.delete(0, END)


# # save Record
# def update_record():
#     selected = cyclo_list.focus()
#     # save new data
#     cyclo_list.item(selected, text="", values=(Version_entry.get(), Capacity_entry.get(), Efficiency_entry.get()))
#
#     # clear entry boxes
#     Version_entry.delete(0, END)
#     Capacity_entry.delete(0, END)
#     Efficiency_entry.delete(0, END)


#Create a button in the main Window to edit  record (open the popup) - cyclotron
cyclotronEditIcon = Image.open("editIcon.jpg")
resizedCycloEditIcon = cyclotronEditIcon.resize((20, 20), Image.ANTIALIAS)
imgEditCyclotron = ImageTk.PhotoImage(resizedCycloEditIcon)
editCyclotronButton = Button(SettingsFrame, image=imgEditCyclotron, borderwidth=0, command=open_popup_cyclotron)
editCyclotronButton.pack(side= LEFT)
editCyclotronButton.place(x=cyclo_Lable_place_x+450, y=cyclo_Lable_place_y+15)

# edit_button = Button(SettingsFrame, text= "Edit", command= open_popup_cyclotron, width=4, height=1)
# edit_button.pack(side= LEFT)
# edit_button.place(x=270, y=265)


#Create a button in the main Window to Delete record - cyclotron
cyclotronDeleteIcon = Image.open("‏‏deleteIcon.png")
resizedCycloDeleteIcon = cyclotronDeleteIcon.resize((20, 20), Image.ANTIALIAS)
imgDeleteCyclotron = ImageTk.PhotoImage(resizedCycloDeleteIcon)
deleteCyclotronButton = Button(SettingsFrame, image=imgDeleteCyclotron, borderwidth=0, command=open_popup_cyclotron)
deleteCyclotronButton.pack(side= LEFT)
deleteCyclotronButton.place(x=cyclo_Lable_place_x+500, y=cyclo_Lable_place_y+15)


#Create a button in the main Window to add record - cyclotron
cyclotronAddIcon = Image.open("addIcon.png")
resizedCycloAddIcon = cyclotronAddIcon.resize((25, 25), Image.ANTIALIAS)
imgAddCyclotron = ImageTk.PhotoImage(resizedCycloAddIcon)
addCyclotronButton = Button(SettingsFrame, image=imgAddCyclotron, borderwidth=0, command=open_popup_cyclotron)
addCyclotronButton.pack(side= LEFT)
addCyclotronButton.place(x=cyclo_Lable_place_x+400, y=cyclo_Lable_place_y+14)

# add_button = Button(SettingsFrame, text="Add Cyclotron", command= open_popup_cyclotron, width = 4, height=1)
# add_button.pack(side= LEFT)
# add_button.place(x=370, y=265)




#
#
# ##################### Module #####################
# # Module Details label
# moduleLabel = Label(SettingsFrame, text = 'Module Details', font=('Helvetica',15, 'bold'),fg='#034672')
# module_Lable_place_x=700
# module_Lable_place_y=70
#
# moduleLabel.pack(side=RIGHT)
# moduleLabel.place(x=module_Lable_place_x,y=module_Lable_place_y)
#
#
# # scrollbar
# Module_scroll = Scrollbar(SettingsFrame ,orient="vertical",width=20)
# Module_scroll.pack(side=RIGHT)
# Module_scroll.place(x=1035, y= 160)
#
# module_list = ttk.Treeview(SettingsFrame, yscrollcommand=Module_scroll.set,height=5)
#
# module_list.pack(side=LEFT, padx=0, pady=module_Lable_place_y+50)
#
#
#
# # Module_scroll.config(command=cyclo_list.yview)
# # Module_scroll.config(command=cyclo_list.xview)
#
# # column define
#
# module_list['columns'] = ('Version', 'Capacity (mci/h)', 'Description')
#
#
# module_list.column("#0", width=0, stretch=NO)
# module_list.column("Version", anchor=CENTER, width=width_Version)
# module_list.column("Capacity (mci/h)", anchor=CENTER, width=width_Capacity)
# module_list.column("Description", anchor=CENTER, width=width_Description)
#
# # Create Headings
# module_list.heading("#0", text="", anchor=CENTER)
# module_list.heading("Version", text="Version", anchor=CENTER)
# module_list.heading("Capacity (mci/h)", text="Capacity (mci/h)", anchor=CENTER)
# module_list.heading("Description", text="Description", anchor=CENTER)
#
# # add data from db
# cursor = db.cursor()
# cursor.execute("SELECT * FROM resourcemodule")
# modules = cursor.fetchall()
#
# iid=0
# for module in modules:
#     print(module)
#     cyclo_list.insert(parent='', index='end', iid=iid, text='',
#                values=(module[1], module[2], module[3]))
#     iid +=1
#
# module_list.pack()
#
# get_version=""
# get_capacity=""
# get_efficiency=""
# get_description=""
#
# def open_popup_module():
#    edit_popup= Toplevel(root)
#    edit_popup.geometry("900x400")
#    edit_popup.title("Edit Module Details")
#    Label(edit_popup, text= "Edit Module Details", font=('Helvetica 17 bold'), fg='#034672').place(x=10,y=18)
#
#    # labels
#    popup_label_y=80
#    Version = Label(edit_popup, text="Version")
#    Version.grid(row=1, column=1)
#    version_x = 20
#    Version.place(x=version_x, y=popup_label_y)
#
#
#    Capacity = Label(edit_popup, text="Capacity")
#    Capacity_units = Label(edit_popup, text="(mci/h)")
#    Capacity_units.config(font=("Courier", 9))
#    Capacity.grid(row=1, column=2)
#    capacity_x = version_x+Version.winfo_reqwidth()+70
#    Capacity.place(x=capacity_x, y=popup_label_y)
#    capacity_units_x=capacity_x + Capacity.winfo_reqwidth()
#    Capacity_units.place(x=capacity_units_x, y=popup_label_y+7)
#
#
#    Description = Label(edit_popup, text="Description")
#    Description.grid(row=1, column=3)
#    description_x = capacity_units_x + Capacity_units.winfo_reqwidth() + 50
#    Description.place(x=description_x, y=popup_label_y)
#
#    # Entry boxes
#    Version_entry = Entry(edit_popup, width=10)
#    Version_entry.grid(row=2, column=1)
#    Version_entry.place(x=version_x+3, y=popup_label_y+30)
#
#    Capacity_entry = Entry(edit_popup, width=14)
#    Capacity_entry.grid(row=2, column=2)
#    Capacity_entry.place(x=capacity_x, y=popup_label_y+30)
#
#
#    Description_entry = Entry(edit_popup,width=15)
#    Description_entry.grid(row=2, column=4)
#    Description_entry.place(x=description_x, y=popup_label_y+30)
#
#
#    # clear entry boxes
#    Version_entry.delete(0, END)
#    Capacity_entry.delete(0, END)
#    Description_entry.delete(0, END)
#
#    # grab record
#    selected = module_list.focus()
#    # grab record values
#    values = module_list.item(selected, 'values')
#    # temp_label.config(text=selected)
#
#    # output to entry boxes
#    Version_entry.insert(0, values[0])
#    Capacity_entry.insert(0, values[1])
#    Description_entry.insert(0, values[2])
#
#    get_version = Version_entry.get()
#    print(get_version)
#    get_capacity = Capacity_entry.get()
#    get_description = Description_entry.get()
#
#    select_button = Button(edit_popup, text="Save Changes", command=update_record)
#    select_button.pack(side=LEFT)
#    select_button.place(x=370, y=250)
#
#
# #Create a button in the main Window to edit  record (open the popup) - module
# moduleEditIcon = Image.open("editIcon.jpg")
# resizedModuleEditIcon = moduleEditIcon.resize((20, 20), Image.ANTIALIAS)
# imgEditModule = ImageTk.PhotoImage(resizedModuleEditIcon)
# editModuleButton = Button(SettingsFrame, image=imgEditModule, borderwidth=0, command=open_popup_module)
# editModuleButton.pack(side= LEFT)
# editModuleButton.place(x=module_Lable_place_x+250, y=module_Lable_place_y+15)
#
# # edit_button = Button(SettingsFrame, text= "Edit", command= open_popup_module)
# # edit_button.pack(side= LEFT)
# # edit_button.place(x=790, y=270)
#
# #Create a button in the main Window to Delete record - module
# moduleDeleteIcon = Image.open("‏‏deleteIcon.png")
# resizedModuleDeleteIcon = moduleDeleteIcon.resize((20, 20), Image.ANTIALIAS)
# imgDeleteModule = ImageTk.PhotoImage(resizedModuleDeleteIcon)
# deleteModuleButton = Button(SettingsFrame, image=imgDeleteModule, borderwidth=0, command=open_popup_module)
# deleteModuleButton.pack(side= LEFT)
# deleteModuleButton.place(x=module_Lable_place_x+300, y=module_Lable_place_y+15)
#
# #Create a button in the main Window to add record - module
# moduleAddIcon = Image.open("addIcon.png")
# resizedModuleAddIcon = moduleAddIcon.resize((25, 25), Image.ANTIALIAS)
# imgAddModule = ImageTk.PhotoImage(resizedModuleAddIcon)
# addModuleButton = Button(SettingsFrame, image=imgAddModule, borderwidth=0, command=open_popup_cyclotron)
# addModuleButton.pack(side= LEFT)
# addModuleButton.place(x=module_Lable_place_x+200, y=module_Lable_place_y+14)
#
# # add_button = Button(SettingsFrame, text="Add", command= open_popup_cyclotron)
# # add_button.pack(side= LEFT)
# # add_button.place(x=890, y=270)
#
# def update_record():
#     selected = cyclo_list.focus()
#     # save new data
#     print("get_version"+get_version)
#     cyclo_list.item(selected, text="", values=(get_version, get_capacity, get_efficiency, get_description))
#
#     # # clear entry boxes
#     # Version_entry.delete(0, END)
#     # Capacity_entry.delete(0, END)
#     # Efficiency_entry.delete(0, END)
#
#
# # # save Record
# # def update_record():
# #     selected = cyclo_list.focus()
# #     # save new data
# #     cyclo_list.item(selected, text="", values=(Version_entry.get(), Capacity_entry.get(), Efficiency_entry.get()))
# #
# #     # clear entry boxes
# #     Version_entry.delete(0, END)
# #     Capacity_entry.delete(0, END)
# #     Efficiency_entry.delete(0, END)


SettingsFrame.pack()
root.mainloop()




