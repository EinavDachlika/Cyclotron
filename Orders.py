from tkinter import *
from tkinter import ttk
import tkinter as tk
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


#root.title("Orders")

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

##################### Start Order page #####################

ordersFrame = Frame(root)
#h = Scrollbar(ordersFrame, orient='horizontal')
ordersFrame.pack(fill=X)


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

my_label=Label(root,text='');

#Empty page/table for new order
OrdersTree = ttk.Treeview(ordersFrame,yscrollcommand=Cyclotron_scroll.set, show='headings', columns=('one', 'two','tree','four','five','six'),height=12)
OrdersTree.pack(side=LEFT, padx=PlaceLable_X+50, pady=PlaceLable_Y+80)

OrdersTree.heading("one", text="1");
OrdersTree.heading("two", text="2");
OrdersTree.heading("tree", text="3");
OrdersTree.heading("four", text="4");
OrdersTree.heading("five", text="5");
OrdersTree.heading("six", text="6");

OrdersTree.insert("" , 0,    text="ID", values=("Hospital","Injection Date","Doses"));
#
# for i in range(3):
#     OrdersTree.insert("", "end", values=(i,"2","30.06.2022","15.00 mCi","00:00"))


#############################Batch quantity Event ######################

BatchList = [
    "0","1","2","3","4","5"
]

status = tk.StringVar()
status.set("0")

#Catch event
def treeBatchselect(event):
    row = OrdersTree.focus()
    if row:
        status.set(OrdersTree.set(row, 'two'))

OrdersTree.bind('<<TreeviewSelect>>', treeBatchselect)

def set_batch(value):
    row = OrdersTree.focus()
    if row:
        OrdersTree.set(row, '1', value)


drop = ttk.OptionMenu(root, status, "0", *BatchList, command=set_batch);
drop.pack();

#############################Batch Event over######################

############################Injection Time event#########################
TimeList = [
    "06:00","06:30","07:00","07:30","08:00","08:30"
]

status = tk.StringVar()
status.set("00:00")

#Catch Injection  event
def InjectionTimeselect(event):
    row = OrdersTree.focus()
    if row:
        status.set(OrdersTree.set(row, 'five'))

OrdersTree.bind('<<TreeviewSelect>>', InjectionTimeselect)

def setInjectionTime(value):
    row = OrdersTree.focus()
    if row:
        OrdersTree.set(row, '4', value)


drop = ttk.OptionMenu(root, status, "00:00", *TimeList, command=setInjectionTime);
drop.pack();

############################Injection Time event over#########################




def importFileFunc():

    def ImportFilefunction():
        """This is function for open Orders  files"""
        filename = fd.askopenfilename(
        initialdir="D:\PythonProjects\Cyclotron",
        title="Open a file",
        filetype=(("Word files","*.docx"),("Word files","*.doc"),("xlsx files","*.xlsx"),("All Files","*.*"),("PDF files","*.pdf")))

        if filename==True :
            if  "xlsx" in filename :                  #Excel file
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



            if "docx" in filename or "doc" in filename:     #word files
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


    # Absorb hosital list data from db
    cursor = db.cursor()
    cursor.execute("SELECT * FROM hospital")
    hospitals_in_db2 = cursor.fetchall()

    #root = tk.Tk()


    ImportFilePage = Toplevel(root);
    ImportFilePage.geometry("900x400");
    ImportFilePage.title("Import File");
    #NewOrdersecondaryPage = tk.Frame(root);

    ImpoerFilePageLabel=Label(ImportFilePage, text="Import File - Order", font=('Helvetica 17 bold'), fg='#034672');
    ImpoerFilePageLabel.pack();

    HospitalListLabel = Label(ImportFilePage, text="Hospital",bg='white');
    HospitalListLabel.pack();
    HospitalListLabel.place(x=20, y=70);
    HospitalList2 = hospitals_in_db2;

    CLickOnHospitalDropMenu2 = StringVar();
    CLickOnHospitalDropMenu2.set("Select Hospital"); #default value

    HospitalDropDown = OptionMenu(ImportFilePage, CLickOnHospitalDropMenu2, *HospitalList2);
    HospitalDropDown.config(width=15,bg='white');#color of dropdown menu
    HospitalDropDown.pack();
    HospitalDropDown.place(x=20, y=100);

    #Create a save button
    saveFileIcon = Image.open("./Images/saveIcon.png");
    save_next_Icon = saveFileIcon.resize((100,50), Image.ANTIALIAS);
    saveImg = ImageTk.PhotoImage(save_next_Icon);
    saveButton=Button(ImportFilePage,image=saveImg, borderwidth=0);
    saveButton.pack();
    saveButton.place(x=250, y=320);

    #Create a Cancel button
    CancelIcon2 = Image.open("./Images/CancelIcon.png");
    resized_Cancel_Icon2 = CancelIcon2.resize((100,50), Image.ANTIALIAS);
    CancelImg2 = ImageTk.PhotoImage(resized_Cancel_Icon2);
    CancelButton2=Button(ImportFilePage,image=CancelImg2, borderwidth=0,command=lambda: [ImportFilePage.destroy()]);#close window-not working
    CancelButton2.pack();
    CancelButton2.place(x=450, y=320);

    #Create a File button+Label
    FileLabel = Label(ImportFilePage, text="File",bg='white');
    FileLabel.pack();
    FileLabel.place(x=500, y=65);

    FileIcon = Image.open("./Images/FileIcon.png")
    resized_File_Icon = FileIcon.resize((60,60), Image.ANTIALIAS)
    file_Image = ImageTk.PhotoImage(resized_File_Icon)
    FileButton=Button(ImportFilePage, image=file_Image, borderwidth=0,command=ImportFilefunction)
    FileButton.pack()
    FileButton.place(x=500, y=95);

    #Create a Injection Date
    InjectionDateLabel = Label(ImportFilePage, text="Injection Date",bg='white');
    InjectionDateLabel.pack();
    InjectionDateLabel.place(x=20, y=180);

    InjectionDateLabel2 = Label(ImportFilePage, text="Pick a date");
    InjectionDateLabel2.pack();
    InjectionDateLabel2.place(x=20, y=210);

    dateLabelEntry = Entry(ImportFilePage,font=("Halvetica",12));
    dateLabelEntry.config(width=25);#width of window
    dateLabelEntry.insert(0, '');
    dateLabelEntry.pack();
    dateLabelEntry.place(x=20, y=240);

    ImportFilePage.pack();




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

#######################Add new order page##########################################
def PopUpForNewOrder():
    def nextButtonSwap():
        """ this function is swap function for viewing New order page,frame 2,after pressing "next" """
        NewOrderMainPage.forget();
        NewOrdersecondaryPage.pack(fill='both',expand=1);

    # def outputSelectedHospital():
    #     HospitalLabelSelected=Label(NewOrdersecondaryPage,text=CLickOnHospitalDropMenu.get())
    #     HospitalLabelSelected.pack();
    # Absorb hosital list data from db
    cursor = db.cursor()
    cursor.execute("SELECT * FROM hospital")
    hospitals_in_db = cursor.fetchall()
    #print(hospitals_in_db);

    """This is function for Add new order page """
    root = tk.Tk()
    root.geometry("900x400");
    root.title("New Order");

    NewOrderMainPage = tk.Frame(root);
    NewOrdersecondaryPage = tk.Frame(root);


    NeworderTitleLabel=Label(NewOrderMainPage, text="New Order", font=('Helvetica 17 bold'), fg='#034672');
    NeworderTitleLabel.pack();
    # labels
    #Create hospital Drop-down menu
    HospitalListLabel = Label(NewOrderMainPage, text="Hospital",bg='white');
    HospitalListLabel.pack();
    HospitalListLabel.place(x=20, y=70);
    HospitalList = hospitals_in_db;

    CLickOnHospitalDropMenu = StringVar();
    CLickOnHospitalDropMenu.set("Select Hospital"); #default value

    HospitalDropDown = OptionMenu(NewOrderMainPage, CLickOnHospitalDropMenu, *HospitalList);
    HospitalDropDown.config(width=20,bg='white');#color of dropdown menu
    HospitalDropDown.pack();
    HospitalDropDown.place(x=20, y=100);

    # val1=CLickOnHospitalDropMenu.get();
    # print(val1)
    #Create Amount of Doses input
    AmountOfDosesLabel = Label(NewOrderMainPage, text="Amount of Doses",bg="white");
    AmountOfDosesLabel.place(x=500, y=80);
    AmountOfDosesLabelEntry = Entry(NewOrderMainPage,font=("Halvetica",12));
    AmountOfDosesLabelEntry.config(width=7);#width of window
    AmountOfDosesLabelEntry.insert(0, '');
    AmountOfDosesLabelEntry.pack();
    AmountOfDosesLabelEntry.place(x=500, y=120);


    #Create Injection time input/entry
    InjectionTimeLabel = Label(NewOrderMainPage, text="Injection Date",bg="white");
    InjectionTimeLabel.place(x=20, y=150);
    InjectionTimeLabelEntry = Entry(NewOrderMainPage,font=("Halvetica",12));
    InjectionTimeLabelEntry.insert(0, '');
    InjectionTimeLabelEntry.pack();
    InjectionTimeLabelEntry.place(x=20, y=180);

    #
    #Create Time range input/Entry
    TimerangeLabel = Label(NewOrderMainPage, text="Time Range",bg="white");
    TimerangeLabel.place(x=500, y=150);
    TimerangeLabelEntry = Entry(NewOrderMainPage,font=("Halvetica",12));
    TimerangeLabelEntry.config(width=7);#width of window
    TimerangeLabelEntry.insert(0, '');
    TimerangeLabelEntry.pack();
    TimerangeLabelEntry.place(x=500, y=180);

    #Create Beginng time input
    AmountOfDosesLabel = Label(NewOrderMainPage, text="Beginning time",bg="white");
    AmountOfDosesLabel.place(x=20, y=240);
    AmountOfDosesLabelEntry = Entry(NewOrderMainPage,font=("Halvetica",12));
    AmountOfDosesLabelEntry.insert(0, '');
    AmountOfDosesLabelEntry.pack();
    AmountOfDosesLabelEntry.place(x=20, y=270);

#################page number 2 at New order window##################
  #  NewOrderMainPage = Toplevel(root);
   # NewOrdersecondaryLabel=Label(NewOrderMainPage, text="New order-page numer 2", font=('Helvetica 17 bold'), fg='#034672').place(x=350, y=18);
    # NewOrdersecondaryLabel.pack();
    # NewOrdersecondaryLabel.geometry("900x400");
    # NewOrdersecondaryLabel.title("New Order");

########################buttons at New page window#######################
    #Create a next button
    nextFileIcon = Image.open("./Images/nextButton.png");
    resized_next_Icon = nextFileIcon.resize((100,50), Image.ANTIALIAS);
    nextImg = ImageTk.PhotoImage(resized_next_Icon);
    NExtFileButton=Button(NewOrderMainPage,text="Next", borderwidth=0,command=nextButtonSwap);
    NExtFileButton.pack();
    NExtFileButton.place(x=210, y=320);

    #Create a Cancel button
    CancelIcon = Image.open("./Images/CancelButton.png");
    resized_Cancel_Icon = CancelIcon.resize((100,50), Image.ANTIALIAS);
    CancelImg = ImageTk.PhotoImage(resized_Cancel_Icon);
    CancelButton=Button(NewOrderMainPage,text="cancel", borderwidth=0,command=lambda: [NewOrderMainPage.destroy()]);#close window-not working
    CancelButton.pack();
    CancelButton.place(x=350, y=320);

#########################secondery page for New order page################
    NewOrdersecondaryLabel=Label(NewOrdersecondaryPage, text="New order", font=('Helvetica 17 bold'), fg='#034672');
    NewOrdersecondaryLabel.place(x=350, y=18);

    # nextFileIcon = Image.open("nextButton.png");
    # resized_next_Icon = nextFileIcon.resize((100,50), Image.ANTIALIAS);
    # nextImg = ImageTk.PhotoImage(resized_next_Icon);
    AddButton=Button(NewOrdersecondaryPage,text="Add", borderwidth=0,command=nextButtonSwap);
    AddButton.pack();
    AddButton.place(x=210, y=320);

    #Create a Cancel button
    # CancelIcon = Image.open("CancelButton.png");
    # resized_Cancel_Icon = CancelIcon.resize((100,50), Image.ANTIALIAS);
    # CancelImg = ImageTk.PhotoImage(resized_Cancel_Icon);
    CancelButton2=Button(NewOrdersecondaryPage,text="cancel", borderwidth=0,command=lambda: [NewOrdersecondaryPage.destroy()]);#close window-not working
    CancelButton2.pack();
    CancelButton2.place(x=350, y=320);


    NewOrderMainPage.pack(fill='both',expand=1);

###############################################################################

    #NewOrderMainPage.mainloop();




###########################Oreders main page#######################################
#Create Search window
searchEntry = Entry(root,font=("Halvetica",12));
searchEntry.insert(0, 'Search Hospital Name');
searchEntry.pack();
searchEntry.place(x=640, y=138);

#Create search icon
searchIcon = Image.open("./Images/SearchButton.png");
resizedSearchedEditIcon = searchIcon.resize((23,23), Image.ANTIALIAS);
SearchImg = ImageTk.PhotoImage(resizedSearchedEditIcon);
SearchLabelicon=Label(image=SearchImg);
SearchLabelicon.pack();
SearchLabelicon.place(x=610, y=135);

#Create edit icon
# editIcon = Image.open("editIcon.jpg")
# resizedEditIcon = editIcon.resize((20,20), Image.ANTIALIAS)
# imgEdit = ImageTk.PhotoImage(resizedEditIcon)
# editButton=Button(ordersFrame, image=imgEdit, borderwidth=0)
# editButton.pack()
# editButton.place(x=425, y=55)

#Create a button for import orders files (Excel or Word)
ImportFileIcon = Image.open("ImportFile2.png")
ImportFileIcon = Image.open("ImportFile2.png")
resized_Edit_Icon = ImportFileIcon.resize((80,20), Image.ANTIALIAS)
img_Edit = ImageTk.PhotoImage(resized_Edit_Icon)
importFileButton=Button(ordersFrame, image=img_Edit, borderwidth=0,command=importFileFunc)
importFileButton.pack()
importFileButton.place(x=230, y=65)

# edit_button = Button(hospitalFrame, text= "Edit", command= open_popup_hospital)
# edit_button.pack(side= LEFT)
# edit_button.place(x=450, y=50)


# Remove button (Icon) - List
deleteIcon = Image.open("./Images/RemoveButton2.png")
resizedDeleteIcon = deleteIcon.resize((105,20), Image.ANTIALIAS)
imgDelete = ImageTk.PhotoImage(resizedDeleteIcon)
deleteButton=Button(ordersFrame, image=imgDelete, borderwidth=0)
deleteButton.pack()
deleteButton.place(x=830, y=65)

#Create New order button
NewOrderIcon = Image.open("./Images/AddnewOrder2.png")
resizedNewOrderIconIcon = NewOrderIcon.resize((120,20), Image.ANTIALIAS)
NewOrderIconimg = ImageTk.PhotoImage(resizedNewOrderIconIcon)
editButton=Button(ordersFrame, image=NewOrderIconimg, borderwidth=0,command=PopUpForNewOrder)
editButton.pack()
editButton.place(x=100, y=65)



root.mainloop()