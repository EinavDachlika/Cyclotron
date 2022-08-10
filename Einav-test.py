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

query = """SELECT h.Name,h.Fixed_activity_level*o.amount as Fixed_activity_level, o.injection_time,o.amount, m.materialName,h.Transport_time_min,h.Transport_time_max
        FROM hospital h INNER JOIN orders o ON  h.idhospital=o.hospitalID INNER JOIN material m ON m.idmaterial=o.materialID
        where Date = '""" + str(date)+""" ' and o.materialID=1
        ORDER BY injection_time """
# print(query)
# query = "SELECT Date FROM orders "
# cursor = db.cursor (db.cursors.DictCursor)

cursor = db.cursor(dictionary=True)
cursor.execute(query)
data = cursor.fetchall()

print('date: ', data)

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

max_activity_batch = 7300

hospitals_output = [] #for output

# hospital_activity = [{}]

# len_batches = len(batches)
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

def sortByTout(hospital):
    return hospital["tout_required"]

def sortByTeos(hospital):
    return hospital["eos_req"]

def change_eos_for_tout(hospital_data, diff):
    Subtract_from_eos = timedelta(minutes=diff)
    last_eos = hospital_data[0]["eos_req"]
    update_eos = last_eos - Subtract_from_eos
    hospital_data[0]["eos_req"] = update_eos

    recursion_for_tout(hospital_data)

def recursion_for_tout(hospital_data,hospitals_output):
    min_to_add = 0
    add_to_tout = timedelta(minutes=min_to_add)
    first_tout = hospital_data[0]["tout_required"]
    for h in hospital_data:
        if h["delivery_order"] == 2:  # secound is will be after QC1 - needed 5 min more
            min_to_add += 5
            add_to_tout = timedelta(minutes=min_to_add)

        Tout_actually = first_tout + add_to_tout
        if Tout_actually > h["tout_required"]:
            if  h["delivery_order"]>1:
                h["delivery_order"]=h["delivery_order"]-1
                recursion_for_tout(hospital_data)
            else: #change eos req
                diff = Tout_actually - h["tout_required"]
                change_eos_for_tout(hospital_data, diff)

        h["Tout_actually"] = Tout_actually
        min_to_add += 5
        add_to_tout = timedelta(minutes=min_to_add)

        hospital_record = next(hospital for hospital in hospitals_output if hospital["Name"] == h['hospital_name'])
        hospital_record['delivery_order'] = h["delivery_order"]

    # return hospital_data
def main_algorithm_calculation():

    for b in batches: #calculate T1,Tout, Tcal,Teos, delivery_order, activity
        if not len(b)==0:
            index = batches.index(b)

            hospitals=[]

            hospital_data =[]
            for order in b:
                hospital_name=order['Name']
                if hospital_name not in hospitals: # order[1] = hospital name in order
                    hospitals.append(hospital_name)

                    #add hospital record to hospitals_output list
                    try:
                        hospital = next(h for h in hospitals_output if h["Name"] == order["Name"] and h["Batch"]==index+1)
                    except:
                        hospitals_output.append({"Name":order["Name"],"Activity":0,'Batch':index+1 })

                    if index != 1:  #condition for choosing Transport_time (min/max) - according to number of batch
                        tout_temp = order['injection_time'] - timedelta(minutes=(order['Transport_time_max'])) #T1-Transport_time
                        hospital_data.append({'hospital_name':hospital_name, "injection_time": order['injection_time'], "Transport_time": order['Transport_time_max'], "tout_required": tout_temp})

                    else:
                        tout_temp = order['injection_time'] - timedelta(minutes=(order['Transport_time_min'])) #T1-Transport_time
                        hospital_data.append({'hospital_name':hospital_name, "injection_time": order['injection_time'], "Transport_time": order['Transport_time_min'], "tout_required": tout_temp})

            hospital_data.sort( key=sortByTout) #sort hospital_data by tout_temp

            #insert Tout
            Tout_key = "Tout"
            i = len(hospital_data[0]) - 1  # last index in the list (Tout_req)
            t_out_final = hospital_data[0]["tout_required"]  # first tout_temp
            batches_general_data[index][Tout_key] = t_out_final

            Hospital_delivery_order=1
            interval_5 = 15
            minutes_for_eos_cal = timedelta(minutes=interval_5)

            for h in hospital_data:
                #delivery_order
                h["delivery_order"] = Hospital_delivery_order
                Hospital_delivery_order+=1

                eos_req = h["tout_required"] - minutes_for_eos_cal  # tout - intervals consider the order
                h["eos_req"] = (eos_req)
                interval_5 += 5
                minutes_for_eos_cal = timedelta(minutes=interval_5)
                # hospital_data.sort(key=sortBy)  # sort hospital_data by tout_eos

            hospital_data.sort(key=sortByTeos)  # sort hospital_data by tout_eos
            recursion_for_tout(hospital_data,hospitals_output)


            # insert Teos - new module
            Teos_key = "Teos"
            t_eos_final = hospital_data[0]["eos_req"] #first index in the list is the shortest time of eos (because it's sorted)
            batches_general_data[index][Teos_key] = t_eos_final


            #insert Tcal - new module
            Tcal_key = "Tcal"
            minutes_for_Tcal_cal = timedelta(minutes=30)
            t_cal = t_out_final + minutes_for_Tcal_cal
            batches_general_data[index][Tcal_key] = t_cal


            # bottles_b = len(hospitals) + 2
            # bottels_key = "bottles_mum"
            # batches_general_data[index][bottels_key] = bottles_b

            batches_general_data[index]["Activity"] = 0  # define the key
            for order in b:
                # insert (A) Activity_Tcal - Activity for Tcal time
                A_Tcal_key = "Activity_Tcal"
                injection_time= order["injection_time"]
                T_cal = batches_general_data[index]["Tcal"]
                A=order["Fixed_activity_level"]

                diff = (injection_time-T_cal).total_seconds() /60  #convert to minutes and then to float
                A_Tcal = math.ceil(A * math.pow((math.e),diff*lamda))  # math.ceil is round up
                order[A_Tcal_key] = A_Tcal


                if batches_general_data[index]["Activity"] + A_Tcal >= max_activity_batch:
                    batches[index+1].append(order)
                    main_algorithm_calculation()

                else:
                    # try:
                    #     hospital = next(h for h in hospitals_output if h["Name"] == order["Name"] and h["Batch"]==index+1)
                    # except:
                    #     hospitals_output.append({"Name":order["Name"],"Activity":0,'Batch':index+1 })
                    hospital = next(h for h in hospitals_output if h["Name"] == order["Name"] and h["Batch"] == index + 1)
                    hospital["Activity"] +=A_Tcal # Hagai - calculate for each bath and hospital separately??

                    batches_general_data[index]["Activity"] += A_Tcal

main_algorithm_calculation()


# #modules
# modules = [1]
#
# for m in modules:
#     previous_module_data_query="""SELECT ROUND(avg(b.EOS_activity/b.DecayCorrected_TTA)*100,0) as Yield_EOB FROM batch b
#                                 where b.resourcemoduleID= """ + str(m) + " ORDER BY b.idbatch LIMIT 7"
#     cursor = db.cursor()
#     cursor.execute(previous_module_data_query)
#     previous_module_data = cursor.fetchall()
#
# #cyclotron
# cyclotron = 2
# previous_cyclotron_data_query="""SELECT b.TargetCurrentLB , rc.constant_efficiency
#                                 FROM batch b JOIN workplan w
#                                 ON b.workplanID=w.idworkplan
#                                 JOIN resourcecyclotron rc
#                                 ON rc.idresourceCyclotron = b.resourcecyclotronID
#                                 where b.resourcecyclotronID= """ + str(cyclotron) + " ORDER BY w.Date LIMIT 1 "
# cursor = db.cursor(dictionary=True)
# cursor.execute(previous_cyclotron_data_query)
# previous_cyclotron_data = cursor.fetchall()
#
# for b in batches_general_data:
#     i=batches_general_data.index(b)
#
#     try:
#         #calculation Activity for batch considering previous modules yields
#         A =round((b["Activity"] * 100) / (previous_module_data[i][0]))
#         b["Activity_considering_yields"] = A
#         # Activity with 5% Confidence percentage
#         A_plus_5 = round(A *1.05)
#         b["Activity_Confidence_percentage"] = A_plus_5
#
#
#         # calculation t
#         K = previous_cyclotron_data_query[0]["constant_efficiency"]
#         I = previous_cyclotron_data_query[0]["TargetCurrentLB"]
#         t = round(  -1 / lamda * ln(1 -A_plus_5/(K*I))  )
#         b["Start_of_exposure_time"] = t
#
#     except:
#         continue
#
#
#
# # cursor.execute(previous_cyclotron_data_query)
# # previous_cyclotron_data = cursor.fetchall()
#
#
#
# print(previous_cyclotron_data)

print("hospitals_output: ",hospitals_output)
print("batches ", batches)
print("batches_general_data: ",batches_general_data)


# root.mainloop()