from tkinter import *
import mysql.connector
from mysql.connector import Error

root = Tk()
root.geometry("300x300")
root.title("Hospitals Details")

hospitalFrame = Frame(root,width=300, height=300)

#defult font
root.option_add("*Font", "Ariel")


# feed label
feedLabel = Label(hospitalFrame, text = 'Add Hospital', font=('Ariel',30, 'bold'),fg='#034672')
feedLabel.place(x=20,y=30)




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
# finally:
#     if db.is_connected():
#         dbCursor.close()
#         db.close()
#         print("MySQL connection is closed")


def insertHospital_OnClick():
    resMess = ""
    if inputHospitalName.get() =="" or inputHospitalTransportTime.get()=="" or inputHospitalFixedActivity.get()=="":
      resMess = "all the fields have to be full"

    else:
      # insert HOSPITAL record to db
      sqlHospital = "INSERT INTO hospital(Name, Fixed_activity_level,Transport_time) VALUES (%s,%s,%s)"
      hospitalRecord = [inputHospitalName.get(), inputHospitalFixedActivity.get(), inputHospitalTransportTime.get()]
      dbCursor.execute(sqlHospital, hospitalRecord)
      db.commit()

      resMess= inputHospitalName.get()+" hospital was successfully added"

    return Label(hospitalFrame, text=resMess).pack()

XfirstPosition = 40
yfirstPosition = 125

# hospital name - label + input
hospitalNameLabel = Label(hospitalFrame, text = 'Hispital Name:', font=('Ariel',14, 'bold'))
hospitalNameLabel.place(x=XfirstPosition,y=yfirstPosition)

inputHospitalName = Entry(hospitalFrame)
inputHospitalName.place(x=XfirstPosition + 140,y=yfirstPosition+5)


# hospital Fixed Activity - label + input
hoapitalFixedActivityLabel = Label(hospitalFrame, text = 'Fixed Activity Lavel:', font=('calibre',14, 'bold'))
hoapitalFixedActivityLabel.place(x=XfirstPosition,y=yfirstPosition+ 80)

inputHospitalFixedActivity = Entry(hospitalFrame)
inputHospitalFixedActivity.place(x=XfirstPosition+200,y=yfirstPosition + 80 +5)


# hospital Transport Time - label + input
hoapitalTransportTimeLabel = Label(hospitalFrame, text = 'Transport Time(minutes):', font=('calibre',14, 'bold'))
hoapitalTransportTimeLabel.place(x=XfirstPosition,y=yfirstPosition + 160)

inputHospitalTransportTime = Entry(hospitalFrame)
inputHospitalTransportTime.place(x=XfirstPosition+245,y=yfirstPosition + 160 +5)

# add hospital button
addHospitalButton = Button(hospitalFrame, text='Add Hospital', command=insertHospital_OnClick,font=('calibre',15, 'bold'), bg="light blue")
addHospitalButton.place(x=100,y=350)


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
