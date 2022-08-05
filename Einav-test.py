from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
from PIL import Image, ImageTk, ImageFont
import mysql.connector
from mysql.connector import Error
from datetime import datetime , date, timedelta
# import xlrd
import xlwt
import openpyxl
from openpyxl import *
from openpyxl.styles import *
from openpyxl.utils import get_column_letter

import math
from numpy import log as ln
import numpy as np

import pandas as pd


from xlwt import Workbook
from tkcalendar import Calendar,DateEntry
import csv
# from importlib import reload


root = Tk()
#root.geometry("300x300")

root.title("Settings")

#defult font
root.option_add("*Font", "Helvetica")


# connect to MySqL
try:

    # # Maor local DB Mysql
    # db = mysql.connector.connect(
    #     host="localhost",
    #     port=3308,
    #     user="root",
    #     password="root",
    #     database="cyclotron")

    # Einav local DB-Mysql
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

# excelIcon = Image.open("excelIcon.png")
# resizedExcelIcon = excelIcon.resize((20, 20), Image.ANTIALIAS)
# imgExcel = ImageTk.PhotoImage(resizedExcelIcon)
# ExcelButton = Button(root, image=imgExcel, borderwidth=0,
#                              command=lambda: root.export_WP_To_Excel())
# # ExcelButton.pack(side=LEFT)
# ExcelButton.place(x= 80, y=80)



cursor = db.cursor()
date= date(2022,8,2)
# print(date)
# query = """SELECT h.Name,h.Fixed_activity_level , o.injection_time,o.amount, m.materialName, o.Date
#         FROM hospital h INNER JOIN orders o ON  h.idhospital=o.hospitalID INNER JOIN material m ON m.idmaterial=o.materialID
#         where Date = '""" + str(date)+""" ' and o.materialID=1
#         ORDER BY hospitalID, injection_time """
# # print(query)
# # query = "SELECT Date FROM orders "
#
# cursor.execute(query)
# data = cursor.fetchall()
# print(data)
# for order in data:
#     print(order)

#
# def exportCsv(result):
#     """Function for creating/exporting Excel file"""
#     print("try exporting new excel file...");
#     headers = ['OrderId', 'Date', 'Injection Time', 'Amount','idhospital','batchID','decayCorrected'];
#     with open('orders.csv','a',newline="") as f:
#         w = csv.writer(f,dialect='excel');
#         messagebox.showinfo("message","Excel file was created");
#         # write the headers
#         w.writerow(headers);
#         for record in result:
#             w.writerow(record);
#
# exportCsv(['OrderId', 'Date', 'Injection Time', 'Amount','idhospital','batchID','decayCorrected'])

# def exportExcel(data):
#     wb = openpyxl.Workbook()
#     # wb.add_format({'text_wrap': True})
#     sheet = wb.active
#     wb.font = Font(size=36, bold=True)
#
#     yellow = "ffff99"
#     #headers
#     headers = ["Dose","Batch","Dose mCi","EOS time", "Cal. Time", "Injection Time", "Decay Time GMP","Decay corrected GMP" ]
#     headers_col_i = 4
#     for header in headers:
#         sheet.cell(row=6, column=headers_col_i).value = header
#         # sheet.cell(row=6, column=headers_col_i).font = Font(size=20, bold=True)
#         sheet.cell(row=6, column=headers_col_i).fill = PatternFill(start_color=yellow, end_color=yellow,
#                                     fill_type="solid")  # bg of hospital cell
#         headers_col_i+=1
#
#     headers2 = ["TIME LEAVES HADASSAH","PRODCUTION SITE","NUMBER OF HOSPITAL VIALS (Not including Hadassah", "TIME USED FOR CALIBRATION", "EOS" ]
#     headers_row_i = 1
#
#     for header in headers2:
#         sheet.cell(row=headers_row_i, column=4).value =header
#         sheet.merge_cells(start_row=headers_row_i, start_column=4, end_row=headers_row_i,
#                                                       end_column=10)
#         headers_row_i+=1
#
#
#     hospitals=[]
#     row_index = 9
#     print(data)
#     for order in data:
#         if order[0] not in hospitals:
#
#             i = 1
#             col_index = 3
#             hospital_orders = [row[1:] for row in data if row[0] == order[0]]
#             end_row_to_merge = row_index+ len(hospital_orders) -1
#
#             hospital_name_cell = sheet.cell(row=row_index, column=col_index)
#             hospital_name_cell.value = order[0] # insert hoapital name to the first col
#             merge_hospital_name_cells = sheet.merge_cells(start_row=row_index, start_column=col_index, end_row=end_row_to_merge, end_column=col_index)
#             wrap_alignment = Alignment(wrap_text=True)
#             hospital_name_cell.alignment = wrap_alignment
#             # hospital_name_cell.font = Font(size=35, bold=True)
#             grey = "c0c0c0"
#             hospital_name_cell.fill = PatternFill(start_color=grey, end_color=grey,
#                                     fill_type="solid")  # bg of hospital cell
#             hospitals.append(order[0])
#             print(hospital_orders)
#             for row in hospital_orders:
#                 DosemCi = row[0] * row[2]
#                 sheet.cell(row=row_index, column=4).value = i  #serial number
#                 # sheet.cell(row=row_index, column=4).font= Font(size=36, bold=True)
#
#                 sheet.cell(row=row_index, column=6).value = DosemCi
#
#                 sheet.cell(row=row_index, column=9).value = str(row[1])   #injection time
#                 # sheet.cell(row=row_index, column=9).font = Font(size=36, bold=True)
#                 i+=1
#                 row_index+=1
#             row_index += 1
#
#
#     wb.save('workplanExce1.xls')
# #
# # exportExcel(data)


# # FilePath = "FDG work plan template.xlsx"
# FilePath = "FDG format.xlsx"
#
# wb = load_workbook(FilePath)


# writer = pd.ExcelWriter(FilePath, engine = 'openpyxl')
# # writer.book = wb
# sheet = wb.active
# sheet=wb['work plan']
#
# hospitals = []
# row_index = 9
# for order in data:
#     if order[0] not in hospitals:
#         grey = "c0c0c0"
#         col_start = 4
#         col_end = 16
#
#         sheet.cell(row=row_index, column=col_start).fill = PatternFill(start_color=grey, end_color=grey,
#                                              fill_type="solid")  # bg of buffer cell
#
#         merge_buffer = sheet.merge_cells(start_row=row_index, start_column=col_start, end_row=row_index,
#                                          end_column=col_end)
#
#         i = 1
#         col_index = 3
#         row_index += 1
#         hospital_orders = [row[1:] for row in data if row[0] == order[0]]
#         end_row_to_merge = row_index + len(hospital_orders) - 1
#         hospital_name_cell = sheet.cell(row=row_index, column=col_index)
#         hospital_name_cell.value = order[0]  # insert hoapital name to the first col
#         merge_hospital_name_cells = sheet.merge_cells(start_row=row_index, start_column=col_index,
#                                                       end_row=end_row_to_merge, end_column=col_index)
#         hospitals.append(order[0])
#
#         for row in hospital_orders:
#             DosemCi = row[0] * row[2]
#             # sheet.cell(row=row_index, column=4).value = i  # serial number
#             # sheet.cell(row=row_index, column=6).value = DosemCi
#             # sheet.cell(row=row_index, column=11).value = str(row[1])  # injection time
#
#             sheet.cell(row=row_index, column=4).value = i  # serial number
#             sheet.cell(row=row_index, column=6).value = DosemCi
#             sheet.cell(row=row_index, column=9).value = str(row[1])  # injection time
#             i += 1
#             row_index += 1


# wb.save('workplanExce020822.xls')


# df = pd.DataFrame([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14],[15,16,17,18,19,20,21]], index=[11,12,13,14,15,16,17],columns=['d', 'e', 'f',',g','h','i','g'])
# df.to_excel(FilePath, sheet_name = 'work plan')
# writer.save()
# writer.close()


#algorithm

query = """SELECT h.Name,h.Fixed_activity_level , o.injection_time,o.amount, m.materialName,h.Transport_time_min,h.Transport_time_max
        FROM hospital h INNER JOIN orders o ON  h.idhospital=o.hospitalID INNER JOIN material m ON m.idmaterial=o.materialID
        where Date = '""" + str(date)+""" ' and o.materialID=1
        ORDER BY hospitalID, injection_time """
# print(query)
# query = "SELECT Date FROM orders "
# cursor = db.cursor (db.cursors.DictCursor)

cursor = db.cursor(dictionary=True)
cursor.execute(query)
data = cursor.fetchall()

print(data)

lamda =  ln(2)/109.6


batch1 = []
batch2 = []
batch3 = []
batch3_exist=True

for order in data:
    order_time = datetime.strptime(str(order["injection_time"]), '%H:%M:%S').time()
    if order_time < datetime.strptime('15:00:00', '%H:%M:%S').time(): #batch 1
        batch1.append(order)

    elif order_time <datetime.strptime('21:00:00', '%H:%M:%S').time():  #batch 2
        batch2.append(order)
    else:   #batch 3
        batch3.append(order)

#chach if batch 3 is exist
dict_batch1_general= {}
dict_batch2_general = {}
dict_batch3_general = {}
batches_general_data = [dict_batch1_general, dict_batch2_general, dict_batch3_general]
batches =[batch1, batch2, batch3]

hospital_activity_output = [] #for output
# len_batches = len(batches)
# hospital_activity = [{}]


# #save empty batches index for removing
# for i  in range(0,len_batches):
#     if len(batches[i])==0:
#         index_to_delete.append(i)
#
# #remove empty batches from list and dictionary
# i=0
# for index in index_to_delete:
#     batches.remove(batches[index-i])
#     del batches_general_data[index-i]
#     i += 1  # removing batch change the index
def sortBy(hospital):
    i = len(hospital) - 1 #last last item in the list
    return hospital[i]

for b in batches: #calculate T1,Tout, Tcal,Teos
    if not len(b)==0:
        index = batches.index(b)

        # T1 - first injection time in batch
        t1_b = b[0]["injection_time"] #first injection time
        T1_key = "T1"
        batches_general_data[index][T1_key] = t1_b

        hospitals=[]
        firts_injectionT_for_hospital = []
        hospital_data =[]
        # number of bottles in a batch
        for order in b:
            hospital_name=order['Name']
            if hospital_name not in hospitals: # order[1] = hospital name in order
                hospitals.append(hospital_name)
                hospital_activity_output.append({'Name':hospital_name,"Activity":0})

                if index != 1:  #condition for choosing Transport_time (min/max) - according to number of batch
                    tout_temp = order['injection_time'] - timedelta(minutes=(order['Transport_time_max']))
                    hospital_data.append([hospital_name, order['injection_time'], order['Transport_time_max'], tout_temp])
                else:
                    tout_temp = order['injection_time'] - timedelta(minutes=(order['Transport_time_min']))
                    hospital_data.append([hospital_name, order['injection_time'], order['Transport_time_min'], tout_temp])

        hospital_data.sort( key=sortBy)
        #insert Tout
        Tout_key = "Tout"
        i = len(hospital_data[0]) - 1   #last index in the list (Tout_req)
        t_out_final = hospital_data[0][i]   # first tout_temp
        batches_general_data[index][Tout_key] = t_out_final

        #insert Tcal - new module
        Tcal_key = "Tcal"
        minutes_for_Tcal_cal = timedelta(minutes=30)
        t_cal = t_out_final + minutes_for_Tcal_cal
        batches_general_data[index][Tcal_key] = t_cal


        interval_5 = 5
        minutes_for_eos_cal = timedelta(minutes=interval_5)
        for h in hospital_data:
            eos_req = h[3] - minutes_for_eos_cal
            h.append(eos_req)
            interval_5+=5
            minutes_for_eos_cal = timedelta(minutes=interval_5)
            hospital_data.sort(key=sortBy )

        # insert Teos - new module
        Teos_key = "Teos"
        i = len(hospital_data[0]) - 1   #last index in the list (eos_req)
        t_eos_final = hospital_data[0][i]
        batches_general_data[index][Teos_key] = t_eos_final


        bottles_b = len(hospitals) + 2
        bottels_key = "bottles_mum"
        batches_general_data[index][bottels_key] = bottles_b


for b in batches:
    if len(b)!= 0 :
        index = batches.index(b)

        for order in b:
            # insert (A) Activity_Tcal - Activity for Tcal time
            A_Tcal_key = "Activity_Tcal"
            injection_time= order["injection_time"]
            T_cal = batches_general_data[index]["Tcal"]
            A=order["Fixed_activity_level"]
            # print(A)
            diff = (injection_time-T_cal).total_seconds() /60  #convert to minutes and then to float
            A_Tcal = A * math.pow((math.e),diff*lamda)
            order[A_Tcal_key] = A_Tcal

            hospital = next(h for h in hospital_activity_output if h["Name"] == order["Name"])
            hospital["Activity"] +=A_Tcal # Hagai - calculate for each bath and hospital separately??



print("hospital_activity_output ",hospital_activity_output)
print(batches)
print(batches_general_data)


# root.mainloop()