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
SettingsFrame.pack(pady=95,padx=85)
# feed label
feedLabel = Label(root, text = 'Settings', font=('Helvetica',26, 'bold'),fg='#034672')
PlaceLable_X=80
PlaceLable_Y=90
feedLabel.place(x=PlaceLable_X,y=PlaceLable_Y)

# Cyclotron Details label
CyclotronLabel = Label(root, text = 'Cyclotron Details', font=('Helvetica',15, 'bold'),fg='#034672')
cyclo_Lable_place_x=120
cyclo_Lable_place_y=150
CyclotronLabel.place(x=cyclo_Lable_place_x,y=cyclo_Lable_place_y)

# game_frame = Frame(root)
# game_frame.pack()

# scrollbar
Cyclotron_scroll = Scrollbar(SettingsFrame)
Cyclotron_scroll.pack(padx=cyclo_Lable_place_x+10)

cyclo_list = ttk.Treeview(SettingsFrame, yscrollcommand=Cyclotron_scroll.set,height=7)

cyclo_list.pack()

# Cyclotron_scroll.config(command=my_game.yview)
# Cyclotron_scroll.config(command=my_game.xview)

# column define

cyclo_list['columns'] = ('Version', 'Capacity (mci/h)', 'Constant Efficiency (mCi/mA)', 'Description')

# column format
cyclo_list.column("#0", width=0, stretch=NO)
cyclo_list.column("Version", anchor=CENTER, width=90)
cyclo_list.column("Capacity (mci/h)", anchor=CENTER, width=110)
cyclo_list.column("Constant Efficiency (mCi/mA)", anchor=CENTER, width=185)
cyclo_list.column("Description", anchor=CENTER, width=110)

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

frame = Frame(root)
frame.pack()


def open_popup():
   edit_popup= Toplevel(root)
   edit_popup.geometry("900x500")
   edit_popup.title("Edit Cyclotron Details")
   Label(edit_popup, text= "Edit Cyclotron Details", font=('Helvetica 14 bold'), fg='#034672').place(x=10,y=18)

   # labels
   popup_label_x=20
   popup_label_y=50
   Version = Label(edit_popup, text="Version")
   Version.grid(row=1, column=1)
   Version.place(x=popup_label_x, y=popup_label_y)

   Capacity = Label(edit_popup, text="Capacity (mci/h)")
   Capacity.grid(row=1, column=2)
   Capacity.place(x=popup_label_x+110, y=popup_label_y)


   Efficiency = Label(edit_popup, text="Constant Efficiency (mCi/mA)")
   Efficiency.grid(row=1, column=3)
   Efficiency.place(x=popup_label_x+90+420, y=popup_label_y)

   Description = Label(edit_popup, text="Description")
   Description.grid(row=1, column=3)
   Description.place(x=popup_label_x+700, y=popup_label_y)


   # Entry boxes
   popup_Entry_x=50
   Version_entry = Entry(edit_popup)
   Version_entry.grid(row=2, column=1)
   Version_entry.place(x=popup_Entry_x, y=popup_label_y+20)

   Capacity_entry = Entry(edit_popup)
   Capacity_entry.grid(row=2, column=2)

   Efficiency_entry = Entry(edit_popup)
   Efficiency_entry.grid(row=2, column=3)

   Description_entry = Entry(edit_popup)
   Description_entry.grid(row=2, column=4)


   # clear entry boxes
   Version_entry.delete(0, END)
   Capacity_entry.delete(0, END)
   Efficiency_entry.delete(0, END)

   # grab record
   selected = cyclo_list.focus()
   # grab record values
   values = cyclo_list.item(selected, 'values')
   # temp_label.config(text=selected)

   # output to entry boxes
   Version_entry.insert(0, values[0])
   Capacity_entry.insert(0, values[1])
   Efficiency_entry.insert(0, values[2])


#Create a button in the main Window to open the popup
edit_button = Button(root, text= "Edit", command= open_popup)
edit_button.pack(pady=10)


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


# # Buttons
# select_button = Button(root, text="Select Record", command= open_popup)
# select_button.pack(pady=10)
#
# edit_button = Button(root, text="Edit ", command=update_record)
# edit_button.pack(pady=10)


temp_label = Label(root, text="")
temp_label.pack()

root.mainloop()




