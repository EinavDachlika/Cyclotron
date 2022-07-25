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

cursor = db.cursor()
cursor.execute("SELECT MAX(idresourceCyclotron) FROM resourcecyclotron")

data = cursor.fetchall()
print(data[0][0])
iid=0
# for recorf in data:
#     val=[]
#     for i in range (0,4): # plus 1 is for the pk that will not show in the table
#         val.append(recorf[i+1])
#     val.append(recorf[0])
# ##################### toolbar #####################
#
# toolbarbgcolor = "white"
# toolbar = Frame(root, bg=toolbarbgcolor)
# toolbar.grid(sticky='nesw')
#
# # add logo - toolbar
# LogoImagePath = Image.open("LogoImage.png")
# LogoImageResize = LogoImagePath.resize((120, 57),Image.ANTIALIAS)
# LogoImage = ImageTk.PhotoImage(LogoImageResize)
# Label(toolbar,image=LogoImage).pack(side=LEFT,padx=10,pady=6)
#
# # work plan button - toolbar
# workPlanButton = Button(toolbar, text="Work Plans",font='Helvetica 11')
# workPlanButton.pack(side=LEFT,padx=10,pady=3)
#
#
# # Hospitals button - toolbar
# hospitalsButton = Button (toolbar, text="Hospitals",font='Helvetica 11', activebackground='gray')
# hospitalsButton.pack(side=LEFT,padx=10,pady=3)
#
# # Orders button - toolbar
# ordersButton = Button (toolbar, text="Orders", font='Helvetica 11')
# ordersButton.pack(side=LEFT,padx=10,pady=3)
#
#
# # Reports button - toolbar
# reportsButton = Button (toolbar, text="Reports", font='Helvetica 11')
# reportsButton.pack(side=LEFT,padx=10,pady=3)
#
# # settings Icon - toolbar
#
# settingsIcon = Image.open("gearIcon.png")
# resizedSettingsIcon = settingsIcon.resize((35,35), Image.ANTIALIAS)
# imgSettings = ImageTk.PhotoImage(resizedSettingsIcon)
# Button(toolbar, image=imgSettings, borderwidth=0).pack(side=RIGHT,padx=10,pady=3)
#
#
# toolbar.pack(side=TOP, fill=X)
#
# toolbar.grid_columnconfigure(1, weight=1)
# ##################### ######## #####################
# SettingsFrame = Frame(root)
# SettingsFrame.pack(fill=X)
# # feed label
# feedLabel = Label(SettingsFrame, text = 'Settings', font=('Helvetica',26, 'bold'),fg='#034672')
# PlaceLable_X=50
# PlaceLable_Y=10
#
# feedLabel.pack(side=LEFT)
# feedLabel.place(x=PlaceLable_X,y=PlaceLable_Y)
#
# # Cyclotron Details label
# CyclotronLabel = Label(SettingsFrame, text = 'Cyclotron Details', font=('Helvetica',15, 'bold'),fg='#034672')
# cyclo_Lable_place_x=80
# cyclo_Lable_place_y=60
#
# CyclotronLabel.pack(side=LEFT)
# CyclotronLabel.place(x=cyclo_Lable_place_x,y=cyclo_Lable_place_y)
#
#
#
# # scrollbar
# Cyclotron_scroll = Scrollbar(SettingsFrame ,orient="vertical",width=20)
# Cyclotron_scroll.pack(side=LEFT)
# Cyclotron_scroll.place(x=613, y= 150)
#
# cyclo_list = ttk.Treeview(SettingsFrame, yscrollcommand=Cyclotron_scroll.set,height=5)
#
# cyclo_list.pack(side=LEFT, padx=cyclo_Lable_place_x+30, pady=cyclo_Lable_place_y+50)
#
# # Cyclotron_scroll.config(command=cyclo_list.yview)
# # Cyclotron_scroll.config(command=cyclo_list.xview)
#
# # column define
#
# cyclo_list['columns'] = ('Version', 'Capacity (mci/h)', 'Constant Efficiency (mCi/mA)', 'Description')
#
# # column format
# width_Version=90
# width_Capacity=110
# width_Efficiency=185
# width_Description=110
#
# cyclo_list.column("#0", width=0, stretch=NO)
# cyclo_list.column("Version", anchor=CENTER, width=width_Version)
# cyclo_list.column("Capacity (mci/h)", anchor=CENTER, width=width_Capacity)
# cyclo_list.column("Constant Efficiency (mCi/mA)", anchor=CENTER, width=width_Efficiency)
# cyclo_list.column("Description", anchor=CENTER, width=width_Description)
#
# # Create Headings
# cyclo_list.heading("#0", text="", anchor=CENTER)
# cyclo_list.heading("Version", text="Version", anchor=CENTER)
# cyclo_list.heading("Capacity (mci/h)", text="Capacity (mci/h)", anchor=CENTER)
# cyclo_list.heading("Constant Efficiency (mCi/mA)", text="Constant Efficiency (mCi/mA)", anchor=CENTER)
# cyclo_list.heading("Description", text="Description", anchor=CENTER)
#
# # add data from db
# cursor = db.cursor()
# cursor.execute("SELECT * FROM resourcecyclotron")
# cyclotrons = cursor.fetchall()
#
# iid=0
# for cyclo in cyclotrons:
#     print(cyclo)
#     cyclo_list.insert(parent='', index='end', iid=iid, text='',
#                values=(cyclo[1], cyclo[2], cyclo[3],cyclo[4]))
#     iid +=1
#
# cyclo_list.pack()
#
# frame = Frame(root)
# frame.pack()
#
# get_version=""
# get_capacity=""
# get_efficiency=""
# get_description=""
#
# def open_popup():
#    edit_popup= Toplevel(root)
#    edit_popup.geometry("900x400")
#    edit_popup.title("Edit Cyclotron Details")
#    Label(edit_popup, text= "Edit Cyclotron Details", font=('Helvetica 17 bold'), fg='#034672').place(x=10,y=18)
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
#    Efficiency = Label(edit_popup, text="Constant Efficiency")
#    Efficiency_units = Label(edit_popup, text="(mCi/mA)")
#    Efficiency_units.config(font=("Courier", 9))
#    Efficiency.grid(row=1, column=3)
#    efficiency_x = capacity_units_x + Capacity_units.winfo_reqwidth() + 50
#    Efficiency.place(x=efficiency_x, y=popup_label_y)
#    efficiency_units_x=efficiency_x + Efficiency.winfo_reqwidth()
#    Efficiency_units.place(x=efficiency_units_x, y=popup_label_y+7)
#
#
#    Description = Label(edit_popup, text="Description")
#    Description.grid(row=1, column=3)
#    description_x = efficiency_units_x+ Efficiency_units.winfo_reqwidth() + 30
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
#    Efficiency_entry = Entry(edit_popup, width=15)
#    Efficiency_entry.grid(row=2, column=3)
#    Efficiency_entry.place(x=efficiency_x, y=popup_label_y+30)
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
#    Efficiency_entry.delete(0, END)
#
#    # grab record
#    selected = cyclo_list.focus()
#    # grab record values
#    values = cyclo_list.item(selected, 'values')
#    # temp_label.config(text=selected)
#
#    # output to entry boxes
#    Version_entry.insert(0, values[0])
#    Capacity_entry.insert(0, values[1])
#    Efficiency_entry.insert(0, values[2])
#    Description_entry.insert(0,values[3])
#
#    get_version = Version_entry.get()
#    print(get_version)
#    get_capacity = Capacity_entry.get()
#    get_efficiency = Efficiency_entry.get()
#    get_description = Description_entry.get()
#
#    select_button = Button(edit_popup, text="Save Changes", command=update_record)
#    select_button.pack(side=LEFT)
#    select_button.place(x=370, y=250)
#
#
# #Create a button in the main Window to open the popup
# edit_button = Button(SettingsFrame, text= "Edit", command= open_popup)
# edit_button.pack(side= LEFT)
# edit_button.place(x=270, y=250)
#
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
#
#
# # Buttons
# select_button = Button(SettingsFrame, text="Add", command= open_popup)
# select_button.pack(side= LEFT)
# select_button.place(x=370, y=250)
#
#
# # temp_label = Label(root, text="")
# # temp_label.pack()
# SettingsFrame.pack()
root.mainloop()




