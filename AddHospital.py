from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error
#maor test
root = Tk()
root.geometry("300x300")


root.title("Add Hospital")


hospitalFrame = Frame(root,width=300, height=300)

#defult font
root.option_add("*Font", "Helvetica")


# feed label
feedLabel = Label(hospitalFrame, text = 'Add Hospital', font=('Helvetica',30, 'bold'),fg='#034672')
feedLabel.place(x=20,y=30)


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

# #Orders menu button - toolbar
# MenuBar = Menu(root)
# root.config(menu=MenuBar)

# def Orders_Onclick():
#         pass
#
# menuOrderButton = Menu(MenuBar, tearoff=0)
# MenuBar.add_cascade(label="Orders", menu=menuOrderButton)
# menuOrderButton.add_command(label = "New Order", command= Orders_Onclick)
# menuOrderButton.add_command(label = "View Orders", command= Orders_Onclick)
#
# #
#
# def Reports_Onclick():
#         pass
#
# menuReportsButton = Menu(MenuBar, tearoff=0)
# MenuBar.add_cascade(label="Reports", menu=menuReportsButton)
# menuReportsButton.add_command(label = "Reports1", command= Reports_Onclick)
# menuReportsButton.add_command(label = "Reports2", command= Reports_Onclick)

# Hospitals button - toolbar
hospitalsButton = Button (toolbar, text="Hospitals",font='Helvetica 12', bg="#B8CAD7", activebackground='gray')
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



# connect to MySqL
try:

    #Maor local DB Mysql
    db = mysql.connector.connect(
        host="localhost",
        port=3308,
        user="root",
        password="root",
        database= "cyclotron")

    #Einav local DB Mysql

  # db = mysql.connector.connect(
  #   host="localhost",
  #   user="root",
  #   password="Cyclotron2022@?%",
  #   database= "cyclotron")

    if db.is_connected():
        # db_Info = db.get_server_info()
        # print("Connected to MySQL Server version ", db_Info)
        dbCursor = db.cursor(buffered=True)
        # dbCursor.execute("select database();")
        # record = dbCursor.fetchone()
        # print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
# finally:
#     if db.is_connected():
#         dbCursor.close()
#         db.close()
#         print("MySQL connection is closed")
# def itsIneger(value):
#     try:
#         int(value)
#         return True
#     except ValueError:
#         return False
#
# def itsFloat(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False

def insertHospital_OnClick():
    resMess = ""
    if inputHospitalName.get() =="" or inputHospitalTransportTime.get()=="" or inputHospitalFixedActivity.get()=="":

        messagebox.showerror("Error","All fields must be filled. Try again")


    else:
      # insert HOSPITAL record to db
      sqlHospital = "INSERT INTO hospital(Name, Fixed_activity_level,Transport_time) VALUES (%s,%s,%s)"
      hospitalRecord = [inputHospitalName.get(), inputHospitalFixedActivity.get(), inputHospitalTransportTime.get()]
      dbCursor.execute(sqlHospital, hospitalRecord)
      db.commit()
      messagebox._show("Hospital added successfully", "The hospital was added successfully")
      inputHospitalName.delete(0,'end')
      inputHospitalTransportTime.delete(0,'end' )
      inputHospitalFixedActivity.delete(0,'end' )


XfirstPosition = 40
yfirstPosition = 125

# hospital name - label + input
hospitalNameLabel = Label(hospitalFrame, text = 'Hospital Name:', font=('Helvetica',14, 'bold'))
hospitalNameLabel.place(x=XfirstPosition,y=yfirstPosition)

inputHospitalName = Entry(hospitalFrame)
inputHospitalName.place(x=XfirstPosition + 150,y=yfirstPosition+5)


# hospital Fixed Activity - label + input
hoapitalFixedActivityLabel = Label(hospitalFrame, text = 'Fixed Activity Lavel:', font=('Helvetica',14, 'bold'))
hoapitalFixedActivityLabel.place(x=XfirstPosition,y=yfirstPosition+ 80)

inputHospitalFixedActivity = Entry(hospitalFrame)
inputHospitalFixedActivity.place(x=XfirstPosition+200,y=yfirstPosition + 80 +5)


# hospital Transport Time - label + input
hoapitalTransportTimeLabel = Label(hospitalFrame, text = 'Transport Time(minutes):', font=('Helvetica',14, 'bold'))
hoapitalTransportTimeLabel.place(x=XfirstPosition,y=yfirstPosition + 160)

inputHospitalTransportTime = Entry(hospitalFrame)
inputHospitalTransportTime.place(x=XfirstPosition+245,y=yfirstPosition + 160 +5)

# add hospital button
addHospitalButton = Button(hospitalFrame, text='Add Hospital', command=insertHospital_OnClick,font=('Helvetica',15, 'bold'), bg="light blue")
addHospitalButton.place(x=XfirstPosition+150 ,y=yfirstPosition+250)


# #show employees from db
# CyclotronCursor.execute("SELECT * FROM employees")
#
# employeesList = CyclotronCursor.fetchall()
#
# for employee in employeesList:
#   print(employee)


hospitalFrame.pack(fill="both", expand=True)
#hospitalFrame.pack()
root.mainloop()

