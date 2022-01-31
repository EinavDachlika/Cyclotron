from tkinter import *
import mysql.connector
from mysql.connector import Error
from tkintertable import TableCanvas, TableModel


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

dbCursor.execute('select * from hospital')
hospitalList =dbCursor.fetchall()

dbCursor.execute('select COUNT(*) from hospital')
rowsInDB =dbCursor.fetchone()[0]  #number of rows(records) in hospital table in DB
print(rowsInDB)

dbCursor.execute("SHOW columns FROM hospital")
sqlHospital= []
for column in dbCursor.fetchall():
    sqlHospital.append(column[0])

sqlHospital=sqlHospital[1:]
print(sqlHospital)

for hospital in hospitalList:
    print(hospital[0])
# selectHodpital =

model = TableModel()
table = TableCanvas(hospitalFrame, model ,
                    #cellwidth=50, cellbackgr='#e3f698',
                    #thefont=('Arial',12),rowheight=18, rowheaderwidth=30,
                    editable=True)

model = table.model
data= sqlHospital
model.importDict(data)
model.addRow(key=nk, Klasa="333")
table.redraw()

hospitalFrame.pack()
root.mainloop()