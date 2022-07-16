from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error
from tkinter import filedialog as fd
import pandas as pd
from docx.api import Document
import aspose.words as aw

##table code
#https://pythonguides.com/python-tkinter-table-tutorial/

root = Tk()
#root.geometry("300x300")


root.title("Orders")

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

##################### Start od Order page #####################

ordersFrame = Frame(root)
h = Scrollbar(ordersFrame, orient='horizontal')
#ordersFrame.pack(fill=X)


# feed label
feedLabel = Label(ordersFrame, text ='Orders', font=('Helvetica', 26, 'bold'), fg='#034672')
PlaceLable_X=50
PlaceLable_Y=10

feedLabel.pack(side=LEFT)
feedLabel.place(x=PlaceLable_X,y=PlaceLable_Y)


# scrollbar
Cyclotron_scroll = Scrollbar(ordersFrame, orient="vertical", width=25)
# Cyclotron_scroll.pack(side=LEFT)
# Cyclotron_scroll.place(x=550, y= 160)

OrdersTree = ttk.Treeview(ordersFrame, yscrollcommand=Cyclotron_scroll.set, height=12)

OrdersTree.pack(side=LEFT, padx=PlaceLable_X+50, pady=PlaceLable_Y+80)
my_label=Label(root,text='');

def openFile():
   """This is function for open Orders excel file"""
   filename = fd.askopenfilename(
       initialdir="D:\PythonProjects\Cyclotron",
       title="Open a file",
       filetype=(("Word files","*.docx"),("Word files","*.doc"),("xlsx files","*.xlsx"),("All Files","*.*"),("PDF files","*.pdf"))
   )
   #print(filename)


   if filename :
     if  "xlsx" in filename :#Excel file
       try:
        filename=r"{}".format(filename)
        df=pd.read_excel(filename)
       except ValueError:
        my_label.config(text="File couldn't be open,try again");
       except FileNotFoundError:
        my_label.config(text="File couldn't be open,try again");

       clear_tree();

       OrdersTree["column"] =  list(df.columns);
       OrdersTree["show"] = "headings";

       for column in OrdersTree["column"]:
        OrdersTree.heading(column,text=column)

       df_rows=df.to_numpy().tolist();

       for row in df_rows:
        OrdersTree.insert("","end",values=row)

        OrdersTree.pack();



     if "docx" in filename or "doc" in filename:#word files
      #convert word to excel

         if (("doc" in filename) and ("docx" not in filename)):#convert docx to doc
             doc = aw.Document(filename)
             filename="NewWordOutput1.docx";
             doc.save(filename)


         document = Document(filename)
         tables = document.tables
         df = pd.DataFrame()

         for table in document.tables:
            for row in table.rows:
                text = [cell.text for cell in row.cells]
                df = df.append([text], ignore_index=True)

         #df.columns = ["Column1", "Column2","Column3","Column4","Column5","Column6","Column7","Column8"]
         df.to_excel("D:/PythonProjects/Cyclotron/OrderOutputTest.xlsx")
         #print(df);


         clear_tree();

         OrdersTree["column"] =  list(df.columns);
         OrdersTree["show"] = "headings";

         for column in OrdersTree["column"]:
            OrdersTree.heading(column,text=column)

         df_rows=df.to_numpy().tolist();

         for row in df_rows:
            OrdersTree.insert("","end",values=row)

            OrdersTree.pack();


# wordFile=open(filename,  errors="ignore");
      # #stuff = wordFile.read();#convert to string
      # new_filename1 = filename.split("/", 3);
      # new_filename2 = new_filename1[3].split(".", 1);
      # tempString=str(new_filename2[0])+".pdf";
      # # # wordFile=open(filename, encoding="Latin-1");
      # # convert(str(new_filename1[3]))
      # # convert(str(new_filename1[3]), str(tempString))
      # # convert("D:\PythonProjects\Cyclotron")
      # pdfFile=PyPDF2.PdfFileReader(str(tempString));
      # # Extract all text fron PDF-if pdf include a couple of pages
      # # count = pdfFile.numPages
      # # for i in range(count):
      # #   page = pdfFile.getPage(i)
      # #   output = []
      # #   output.append(page.extractText())
      # page=pdfFile.getPage(0);#Extract only from first page
      # page_stuff=page.extractText();
      # print(page_stuff);
      # #not working need to be with text box and not tree
      # for i in range(len(page_stuff)):
      #  OrdersTree.insert('', 'end',values=i)
      # #OrdersTree.insert(1.0,page_stuff);#not working well-need to be fixed-need to be with text box and not trre
      # OrdersTree.pack();
      # wordFile.close();





def clear_tree():
    OrdersTree.delete(*OrdersTree.get_children())



#
# # Cyclotron_scroll.config(command=cyclo_list.yview)
# # Cyclotron_scroll.config(command=cyclo_list.xview)
#
# # column define
#
# hospitals_list['columns'] = ('Quantity', 'Injection time', 'Activation','Comments')
#
# # column format
# width_Version=110
# width_Capacity=110
# width_Efficiency=185
# width_Description=110
#
# hospitals_list.column("#0", width=0, stretch=NO)
# hospitals_list.column("Quantity", anchor=CENTER, width=width_Version)
# hospitals_list.column("Injection time", anchor=CENTER, width=width_Capacity)
# hospitals_list.column("Activation", anchor=CENTER, width=width_Efficiency)
# hospitals_list.column("Comments", anchor=CENTER, width=width_Efficiency)
#
# # Create Headings
# hospitals_list.heading("#0", text="", anchor=CENTER)
# hospitals_list.heading("Quantity", text="Name", anchor=CENTER)
# hospitals_list.heading("Injection time", text="Injection time", anchor=CENTER)
# hospitals_list.heading("Activation", text="Activation", anchor=CENTER)
# hospitals_list.heading("Comments", text="Comments", anchor=CENTER)
#
# # add data from db
# cursor = db.cursor()
# cursor.execute("SELECT * FROM hospital")
# hospitals_in_db = cursor.fetchall()
#
# iid=0
# for hospital in hospitals_in_db:
#     #print(hospital)
#     hospitals_list.insert(parent='', index='end', iid=iid, text='',
#                           values=(hospital[1], hospital[2], hospital[3]))
#     iid +=1
#
# hospitals_list.pack()



# def open_popup_hospital():
#     pass
#
# def delete_hospital():
#     pass
###################Buttons for edit,delete,import file and etc.###################################
#Create a button in the main Window to open the popup
# edit_button = Button(hospitalFrame, text= "Edit", command= open_popup_hospital)
# edit_button.pack(side= LEFT)
# edit_button.place(x=450, y=50)
# edit_button.pack(side=LEFT, padx=PlaceLable_X+100, pady=PlaceLable_Y+50)

#Create a button in the main Window to open the popup
editIcon = Image.open("editIcon.jpg")
resizedEditIcon = editIcon.resize((20,20), Image.ANTIALIAS)
imgEdit = ImageTk.PhotoImage(resizedEditIcon)
editButton=Button(ordersFrame, image=imgEdit, borderwidth=0)
editButton.pack()
editButton.place(x=425, y=55)

#Create a button for import order from files(Excel or Word)
ImportFileIcon = Image.open("imporFile.png")
resized_Edit_Icon = ImportFileIcon.resize((20,20), Image.ANTIALIAS)
img_Edit = ImageTk.PhotoImage(resized_Edit_Icon)
importFileButton=Button(ordersFrame, image=img_Edit, borderwidth=0,command=openFile)
importFileButton.pack()
importFileButton.place(x=380, y=55)

# edit_button = Button(hospitalFrame, text= "Edit", command= open_popup_hospital)
# edit_button.pack(side= LEFT)
# edit_button.place(x=450, y=50)


# delete button (Icon) - List
deleteIcon = Image.open("‏‏deleteIcon.png")
resizedDeleteIcon = deleteIcon.resize((20,20), Image.ANTIALIAS)
imgDelete = ImageTk.PhotoImage(resizedDeleteIcon)
deleteButton=Button(ordersFrame, image=imgDelete, borderwidth=0)
deleteButton.pack()
deleteButton.place(x=470, y=55)




root.mainloop()