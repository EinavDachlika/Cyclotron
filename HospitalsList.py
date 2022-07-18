from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error

##table code
#https://pythonguides.com/python-tkinter-table-tutorial/

root = Tk()
#root.geometry("300x300")


root.title("Hospital list")

#defult font
root.option_add("*Font", "Helvetica")

# connect to MySqL
try:
    #Maor local DB Mysql
    db = mysql.connector.connect(
        host="localhost",
        port=3308,
        user="root",
        password="root",
        database= "cyclotron")


# #Einav local DB Mysql
#   db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Cyclotron2022@?%",
#     database= "cyclotron")

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

##################### Hospitals List #####################

hospitalFrame = Frame(root)
h = Scrollbar(hospitalFrame, orient='horizontal')
hospitalFrame.pack(fill=X)


# feed label
feedLabel = Label(hospitalFrame, text = 'Hospitals Details', font=('Helvetica',26, 'bold'),fg='#034672')
PlaceLable_X=50
PlaceLable_Y=10

feedLabel.pack(side=LEFT)
feedLabel.place(x=PlaceLable_X,y=PlaceLable_Y)


# scrollbar
Cyclotron_scroll = Scrollbar(hospitalFrame ,orient="vertical",width=25)
# Cyclotron_scroll.pack(side=LEFT)
# Cyclotron_scroll.place(x=550, y= 160)

hospitals_list = ttk.Treeview(hospitalFrame, yscrollcommand=Cyclotron_scroll.set,height=12)

hospitals_list.pack(side=LEFT, padx=PlaceLable_X+50, pady=PlaceLable_Y+80)

# Cyclotron_scroll.config(command=cyclo_list.yview)
# Cyclotron_scroll.config(command=cyclo_list.xview)

# column define

hospitals_list['columns'] = ('Name', 'Fixed Activity Level (mci)', 'Transport Time (minutes)')

# column format
width_Version=110
width_Capacity=110
width_Efficiency=185
width_Description=110

hospitals_list.column("#0", width=0, stretch=NO)
hospitals_list.column("Name", anchor=CENTER, width=width_Version)
hospitals_list.column("Fixed Activity Level (mci)", anchor=CENTER, width=width_Capacity)
hospitals_list.column("Transport Time (minutes)", anchor=CENTER, width=width_Efficiency)

# Create Headings
hospitals_list.heading("#0", text="", anchor=CENTER)
hospitals_list.heading("Name", text="Name", anchor=CENTER)
hospitals_list.heading("Fixed Activity Level (mci)", text="Fixed Activity Level (mci)", anchor=CENTER)
hospitals_list.heading("Transport Time (minutes)", text="Transport Time (minutes)", anchor=CENTER)

# add data from db
cursor = db.cursor()
cursor.execute("SELECT * FROM hospital")
hospitals_in_db = cursor.fetchall()

#Insert data of Hospitals into My-SQl
#The INSERT IGNORE statement will cause MySQL to do nothing when the insertion throws an error. If there’s no error, then a new row will be added to the table.
cursor.execute("INSERT IGNORE INTO hospital (idhospital,Name,Fixed_activity_level,Transport_time) VALUES (1,'Belinson',9.2,15.0),(2,'Ichilov',10.0,20.0),(3,'Assuta TA',10.9,30.0),(4,'Sheb',10.5,35.0),(5,'Ziv',11.0,25.0),(6,'Assuta Ashdod',13.1,60.0),(7,'Assaf Harofeh',10.6,65.0),(8,'Augusta Victoria',9.6,50.0),(9,'Hila Pharma',9.6,50.0),(10,'Hadassah',9.5,0.0);")
#cleanup

#Commit changes in DB
db.commit()

cursor.close()

#Close connection to DB
db.close()

iid=0
for hospital in hospitals_in_db:
    #print(hospital)
    hospitals_list.insert(parent='', index='end', iid=iid, text='',
               values=(hospital[1], hospital[2], hospital[3]))
    iid +=1

hospitals_list.pack()



def open_popup_hospital():
    pass

def delete_hospital():
    pass

#Create a button in the main Window to open the popup
# edit_button = Button(hospitalFrame, text= "Edit", command= open_popup_hospital)
# edit_button.pack(side= LEFT)
# edit_button.place(x=450, y=50)
# edit_button.pack(side=LEFT, padx=PlaceLable_X+100, pady=PlaceLable_Y+50)

#Create a button in the main Window to open the popup
editIcon = Image.open("editIcon.jpg")
resizedEditIcon = editIcon.resize((20,20), Image.ANTIALIAS)
imgEdit = ImageTk.PhotoImage(resizedEditIcon)
editButton=Button(hospitalFrame, image=imgEdit, borderwidth=0, command=delete_hospital)
editButton.pack()
editButton.place(x=425, y=55)

# edit_button = Button(hospitalFrame, text= "Edit", command= open_popup_hospital)
# edit_button.pack(side= LEFT)
# edit_button.place(x=450, y=50)


# delete button (Icon) - List
deleteIcon = Image.open("‏‏deleteIcon.png")
resizedDeleteIcon = deleteIcon.resize((20,20), Image.ANTIALIAS)
imgDelete = ImageTk.PhotoImage(resizedDeleteIcon)
deleteButton=Button(hospitalFrame, image=imgDelete, borderwidth=0, command=delete_hospital)
deleteButton.pack()
deleteButton.place(x=470, y=55)



#hospitalFrame.pack()

root.mainloop()