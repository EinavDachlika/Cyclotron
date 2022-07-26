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
from tkcalendar import Calendar,DateEntry
from datetime import datetime

##table code
#https://pythonguides.com/python-tkinter-table-tutorial/

root = tk.Tk();
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

##################### Start Order page ###################################################

ordersFrame = Frame(root);

#h = Scrollbar(ordersFrame, orient='horizontal')
ordersFrame.pack(fill=X)


# feed label
feedLabel = Label(ordersFrame, text ='Orders', font=('Helvetica', 26, 'bold'), fg='#034672');
feedLabel.pack(side=LEFT);
feedLabel.place(x=50,y=10);


# scrollbar
Cyclotron_scroll = Scrollbar(ordersFrame, orient="vertical", width=25)
# Cyclotron_scroll.pack(side=LEFT)
# Cyclotron_scroll.place(x=550, y= 160)

#my_label=Label(root,text='');

#Empty page/table for new order
OrdersTree = ttk.Treeview(ordersFrame,yscrollcommand=Cyclotron_scroll.set,columns=('1', '2'),height=20)
OrdersTree['show'] = 'tree headings';
OrdersTree.pack(side=LEFT, padx=100, pady=110)

#Foramte Columns
OrdersTree.column("#0");
OrdersTree.column("1");
OrdersTree.column("2");

#Define headers/titles in table
OrdersTree.heading("#0", text="Hospital");
OrdersTree.heading("1", text="Injection Date");
OrdersTree.heading("2", text="Doses");
#
# for i in range(3):
#     OrdersTree.insert("", "end", values=(i,"2","30.06.2022"))


def importFileFunc():
    TempList=["",""];
    def ImportFilefunction():

        """This is function for open Orders  files"""
        filename = fd.askopenfilename(
        initialdir="D:\PythonProjects\Cyclotron",
        title="Open a file",
        filetype=(("Word files","*.docx"),("Word files","*.doc"),("Excel files","*.xlsx"),("All Files","*.*"),("PDF files","*.pdf")))

        if filename:
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
    cursor.execute("SELECT Name FROM hospital")
    hospitals_in_db2 = cursor.fetchall()

################################################Import File page###########################

    ImportFilePage = Toplevel(root);
    ImportFilePage.geometry("900x400");
    ImportFilePage.config(bg="#F0F3F4");#color of page-white-gray
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

    # def my_upd(*args):                                    # triggered when value of string varaible changes
    #     l1.config(text=CLickOnHospitalDropMenu2.get());
    #     # read and display date
    #
    # l1=tk.Label(ImportFilePage);  # Label to display date
    # print(type(l1));
    # l1.pack();
    #
    # CLickOnHospitalDropMenu2.trace('w',my_upd) ;#
    # on change of string variable
    #val1=CLickOnHospitalDropMenu2.get();
    #print(val1)
    def HospitalChoosecallback(selection):
           ChoosenHospital=selection;
           TempList[0]=ChoosenHospital[1];
           print(TempList[0])
           # for i in range(30):
           #  OrdersTree.insert("", "end", values=(ChoosenHospital[1]));
           #print(selection[1]);
           return ChoosenHospital;

    HospitalDropDown = OptionMenu(ImportFilePage, CLickOnHospitalDropMenu2, *HospitalList2,command=HospitalChoosecallback);
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
    InjectionDateLabel2 = Label(ImportFilePage, text="Pick a date",fg="gray",font=("Halvetica",10));#fg=color of text
    InjectionDateLabel2.pack();
    InjectionDateLabel2.place(x=20, y=210);

    #Calender
    #add calender icon
    CalendarIcon = Image.open("./Images/CalendarIcon.png");
    resizedCalenderIcon = CalendarIcon.resize((23,23), Image.ANTIALIAS);
    CalenderImg = ImageTk.PhotoImage(resizedCalenderIcon);
    CalenderLabelicon=Label(ImportFilePage,image=CalenderImg);
    CalenderLabelicon.pack();
    CalenderLabelicon.place(x=180, y=238);


    #Add calender widget/method
    sel=tk.StringVar() # declaring string variable
    def print_sel(e):
        ChoosenDate=cal.get_date();
        TempList[1]=ChoosenDate;
        print( TempList[1]);
        # if ((counter==0) or (counter==null)):
        counter=0;
        #Loop throw the tree/table
        for recordInrow in range(len(TempList)-1):
         OrdersTree.insert(parent="",index= "end",iid=counter, values=(TempList[0],TempList[1]));
         OrdersTree.insert(parent=counter,index= "end",iid=counter+2,text=TempList[0]);
         counter=counter+1;

    cal1=DateEntry(ImportFilePage,selectmode='day',textvariable=sel);
    cal1.pack(pady = 20);
    cal1.place(x=20, y=240);
    cal1.bind("<<DateEntrySelected>>", print_sel);#catch date event
    # for i in range(len(page_stuff)):
    #  OrdersTree.insert('', 'end',values=i)
    #OrdersTree.insert(parent='', index=0, text='', values=(TempList[0],TempList[1]));


    # def my_upd(*args): # triggered when value of string varaible changes
    #     l1.config(text=sel.get()); # read and display date
    #
    # l1=tk.Label(ImportFilePage,bg='yellow');  # Label to display date
    # l1.pack();
    #
    # sel.trace('w',my_upd) ;# on change of string variable
    # print(sel);

    #print(TempList);
    ImportFilePage.mainloop();




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


############################new order page#########################################

def PopUpForNewOrder():
    # def nextButtonSwap():
    #     """ this function is swap function for viewing New order page,frame 2,after pressing "next" """
    #     NewOrderMainPage.forget();
    #     NewOrdersecondaryPage.pack(fill='both',expand=1);

    # def outputSelectedHospital():
    #     HospitalLabelSelected=Label(NewOrdersecondaryPage,text=CLickOnHospitalDropMenu.get())
    #     HospitalLabelSelected.pack();
    # Absorb hosital list data from db
    cursor = db.cursor()
    cursor.execute("SELECT idhospital,Name FROM hospital")
    hospitals_in_db = cursor.fetchall()
    #print(type(hospitals_in_db[0]));#List of hospitals

    """This is function for Add new order page """
    #root = tk.Tk()


    NewOrderMainPage =Toplevel(root);
    NewOrderMainPage.title("New Order");
    NewOrderMainPage.geometry("1200x600");
    NewOrderMainPage.config(bg="#F0F3F4");#Color of page(White-Gray)

    #NewOrderMainPage.place(x=450,y=70);

    #NewOrdersecondaryPage = tk.Frame(root);


#########################page number 1,New order page#########################################################
    NeworderTitleLabel=Label(NewOrderMainPage, text="New Order #1",bg="#F0F3F4", font=('Helvetica 17 bold'), fg='#034672');
    NeworderTitleLabel.pack();
    NeworderTitleLabel.place(x=200,y=25);
    # labels
    #Create hospital Drop-down menu

    HospitalListLabel = Label(NewOrderMainPage, text="Hospital",bg='white');
    HospitalListLabel.pack();
    HospitalListLabel.place(x=20, y=70);
    HospitalList2 = hospitals_in_db;

    def HospitalChoosecallback2(HosiptalSelection):
        global hospitalId;
        """This function is to catch Hopital name event and past/print it to page number 2 """
        HospitalLabel2=Label(NewOrderMainPage, text=CLickOnHospitalDropMenu.get(),bg="white", font=('Helvetica 14'));
        x=CLickOnHospitalDropMenu.get();#string type here
        #print(x);
        hospitalLabel = x.split(",",1);
        hospitalNameTemp=hospitalLabel[1];
        #print(hospitalNameTemp);
        hospitalIDTemp=hospitalLabel[0];
        #print(hospitalIDTemp);
        HospitalID=hospitalIDTemp.split("(");
        hospitalId=int(HospitalID[1]);

        HospitalLabel2.pack();
        HospitalLabel2.place(x=650,y=80);

        # for i in range(30):
        #  OrdersTree.insert("", "end", values=(ChoosenHospital[1]));
        #print(selection[1]);

    CLickOnHospitalDropMenu = StringVar();
    CLickOnHospitalDropMenu.set("Select Hospital"); #default value

    HospitalDropDown = OptionMenu(NewOrderMainPage, CLickOnHospitalDropMenu, *HospitalList2,command=HospitalChoosecallback2);
    HospitalDropDown.config(width=12,bg='white');#color of dropdown menu
    HospitalDropDown.pack();
    HospitalDropDown.place(x=20, y=100);

    # declaring string variable for storing amount
    amountVar=tk.StringVar();
    endOftimeVar=tk.StringVar();
    # declaring string variable for storing time
    HoursVar = StringVar();
    MinutesVar = StringVar();
    global OrderID;
    OrderID=0;
    global idCounter;
    ListofVal=["","","","","",""];
    def submit():
        global hospitalId;
        global OrderID;
        #Initialization-clear all the records
        for rawselected in NewOrderTree_P2.get_children():
         NewOrderTree_P2.delete(rawselected);

        #Get Time varibles avent,hous and minutes
        EndOfTime=endOftimeVar.get();
        Minutes_Var=MinutesVar.get();
        Hours_Var=HoursVar.get();
        #BeginigHour=Hours_Var+":"+Minutes_Var;
        #get amount event variable
        amount=amountVar.get();
        IntAmount=(int(amount));
        ListofVal[0]=idCounter=0;
        ListofVal[1]=amountIndividual=(IntAmount/IntAmount);
        ListofVal[2]=int(Hours_Var);
        ListofVal[3]=int(Minutes_Var);
        ListofVal[4]=IntAmount;
        ListofVal[5]=hospitalId;

        #Enter data to the the table
        # for idCounter,j in zip(range(IntAmount),range(BeginigHour,IntAmount)):
        #     NewOrderTree_P2.insert("", "end", values=(idCounter,amount2,j));
        for record in range(int(IntAmount)):
            NewOrderTree_P2.insert("", "end",values=( ListofVal[0],ListofVal[1],f'{ListofVal[2]}:{ListofVal[3]}'));
            ListofVal[2]=ListofVal[2]+1;
            ListofVal[3]=ListofVal[3]+30;
            ListofVal[0]= ListofVal[0]+1;

        OrderID+=1;#counterID=counterID+1
        #print(OrderID);
        amountVar.set("");
        MinutesVar.set("");
        HoursVar.set("");



    #Create Amount of Doses input
    AmountOfDosesLabel = Label(NewOrderMainPage, text="Amount of Doses",bg="white");
    AmountOfDosesLabel.place(x=400, y=80);

    AmountOfDosesLabelEntry = Entry(NewOrderMainPage,textvariable=amountVar,font=("Halvetica",12));
    AmountOfDosesLabelEntry.config(width=7);#width of window
    # amount=AmountOfDosesLabelEntry.get();
    # print(amount);
    AmountOfDosesLabelEntry.insert(0, '');
    AmountOfDosesLabelEntry.pack();
    AmountOfDosesLabelEntry.place(x=400, y=120);


    #Create Injection time input/entry
    InjectionTimeLabel = Label(NewOrderMainPage, text="Injection Date",bg="white");
    InjectionTimeLabel.place(x=20, y=200);

    #Calender
    #add calender icon
    CalendarIcon1 = Image.open("./Images/CalendarIcon.png");
    resizedCalenderIcon1 = CalendarIcon1.resize((23,23), Image.ANTIALIAS);
    CalenderImg1 = ImageTk.PhotoImage(resizedCalenderIcon1);
    CalenderLabelicon1=Label(NewOrderMainPage,image=CalenderImg1);
    CalenderLabelicon1.pack();
    CalenderLabelicon1.place(x=180, y=238);


    #Add calender widget/method
    selectDateEvent=tk.StringVar() # declaring string variable
    def print_sel(e):
        global ChoosenDate;
        """ This function print to the tree/table """
        ChoosenDate=cal.get_date();
        #print(ChoosenDate);
        #copy and past date event to page number 2
        dateLabel2=Label(NewOrderMainPage, text= ChoosenDate,bg="white", font=('Helvetica 14'));
        dateLabel2.pack();
        dateLabel2.place(x=760,y=80);
        # TempList[1]=ChoosenDate;
        # print( TempList[1]);
        # if ((counter==0) or (counter==null)):
        # counter=0;
        # #Loop throw the tree/table
        # for recordInrow in range(len(TempList)-1):
        #     OrdersTree.insert(parent="",index= "end",iid=counter, values=(TempList[0],TempList[1]));
        #     OrdersTree.insert(parent=counter,index= "end",iid=counter+2,text=TempList[0]);
        #     counter=counter+1;

    cal=DateEntry(NewOrderMainPage,selectmode='day',textvariable=selectDateEvent);
    cal.pack(pady = 20);
    cal.config(width=20);#width of window
    cal.place(x=20, y=240);
    cal.bind("<<DateEntrySelected>>", print_sel);#catch date event



# InjectionTimeLabelEntry = Entry(NewOrderMainPage,font=("Halvetica",12));
    # InjectionTimeLabelEntry.insert(0, '');
    # InjectionTimeLabelEntry.pack();
    # InjectionTimeLabelEntry.place(x=20, y=180);

    #
    #Create Time range input/Entry
    TimerangeLabel = Label(NewOrderMainPage, text="Time Range/End time",bg="white");
    TimerangeLabel.place(x=400, y=200);
    TimerangeLabelEntry = Entry(NewOrderMainPage,textvariable=endOftimeVar,font=("Halvetica",12));
    TimerangeLabelEntry.config(width=7);#width of window
    TimerangeLabelEntry.insert(0, '');
    TimerangeLabelEntry.pack();
    TimerangeLabelEntry.place(x=400, y=240);

    #Create Beginng time input
    AmountOfDosesLabel = Label(NewOrderMainPage, text="Beginning time",bg="white");
    AmountOfDosesLabel.place(x=20, y=300);
    # AmountOfDosesLabelEntry = Entry(NewOrderMainPage,font=("Halvetica",12));
    # AmountOfDosesLabelEntry.insert(0, '');
    # AmountOfDosesLabelEntry.pack();
    # AmountOfDosesLabelEntry.place(x=20, y=270);
    InjectionDateLabel2 = Label(NewOrderMainPage, text="Pick a time",fg="gray",font=("Halvetica",10));#fg=color of text
    InjectionDateLabel2.pack();
    InjectionDateLabel2.place(x=20, y=330);

    ################FIxed hour,minutes,and secondes########################
    #Hours
    sp1 = Spinbox(NewOrderMainPage,textvariable=HoursVar,from_= 0, to = 24,wrap=True,width=2);
    sp1.pack();
    sp1.place(x=20, y=350);
    # Minutes
    sp2 = Spinbox(NewOrderMainPage,textvariable=MinutesVar ,from_= 0, to = 59,wrap=True,width=2);
    sp2.pack();
    sp2.place(x=65, y=350);

    #Submit/Next button
    global NextButton;
    nextIcon = Image.open("./Images/nextButton.png");
    resized_next_Icon = nextIcon.resize((100,50), Image.ANTIALIAS);
    NextButton = ImageTk.PhotoImage(resized_next_Icon);
    sub_btn=tk.Button(NewOrderMainPage ,image=NextButton, command = submit,borderwidth=0)
    sub_btn.pack();
    sub_btn.place(x=65, y=530)



    #####################################New order page numer 2###################################################

    NewOrdersecondaryLabel=Label(NewOrderMainPage, text="New Order #2",bg="#F0F3F4", font=('Helvetica 17 bold'), fg='#034672');
    NewOrdersecondaryLabel.pack();
    NewOrdersecondaryLabel.place(x=900,y=27);


    def enterToDB():#Function to insert data into My-SQL Db
     # ValuseDic = {
     #        'idorders': 4,
     #        'Date': '2002-03-92',
     #        'injection_time': '11:20:11',
     #        'amount': 7,
     #        'hospitalID': 7,
     #        'batchID': 7,
     #        'DecayCorrected': 7 }  ;
     cursor = db.cursor(buffered=True);
     for i in range(ListofVal[4]):
      ValuseTuple=(OrderID,ChoosenDate,"11:20:11",ListofVal[1], ListofVal[5],0,0);
      print("order trying to get in DB-Add pressed");
      cursor.execute("INSERT INTO orders (idorders,Date,injection_time,amount,hospitalID,batchID,DecayCorrected) VALUES (%s,%s,%s,%s,%s,%s,%s);",ValuseTuple)

    #Commit changes in DB
     db.commit()
     cursor.close()
     #Close connection to DB
     #db.close()

    #Create ADD button
    global addImg;
    AddFileIcon = Image.open("./Images/AddButton.png");
    resized_add_Icon = AddFileIcon.resize((100,50), Image.ANTIALIAS);
    addImg = ImageTk.PhotoImage(resized_add_Icon);
    AddButton=Button(NewOrderMainPage,image=addImg, borderwidth=0,command=enterToDB);
    AddButton.pack();
    AddButton.place(x=850, y=520);

    #Create a Cancel button
    global CancelImg;
    CancelIcon = Image.open("./Images/CancelButton.png");
    resized_Cancel_Icon = CancelIcon.resize((100,50), Image.ANTIALIAS);
    CancelImg = ImageTk.PhotoImage(resized_Cancel_Icon);
    CancelButton2=Button(NewOrderMainPage,image=CancelImg, borderwidth=0,command=lambda: [NewOrderMainPage.destroy()]);#close window-not working
    CancelButton2.pack();
    CancelButton2.place(x=1000, y=520);


    #Empty page/table for new order,create New tree for page 2
    NewOrderTree_P2 = ttk.Treeview(NewOrderMainPage,yscrollcommand=Cyclotron_scroll.set,height=15);
    NewOrderTree_P2['columns']= ("ID","Amount","Injection time")
    #NewOrderTree_P2['show'] = 'tree headings';
    NewOrderTree_P2.pack();
    NewOrderTree_P2.place(x=750,y=130);
    #Foramte Columns
    NewOrderTree_P2.column("#0",width=0,minwidth=0);
    NewOrderTree_P2.column("ID",anchor=W,width=80,minwidth=25);
    NewOrderTree_P2.column("Amount",anchor=CENTER,width=120,minwidth=25);
    NewOrderTree_P2.column("Injection time",anchor=W,width=120,minwidth=25);

    #Define headers/titles in table
    NewOrderTree_P2.heading("#0", text="Label",anchor=W);
    NewOrderTree_P2.heading("ID", text="ID",anchor=W);
    NewOrderTree_P2.heading("Amount", text="Amount",anchor=CENTER);
    NewOrderTree_P2.heading("Injection time", text="Injection time",anchor=W);

    #############################Amount quantity Event ######################

    AmountList = [
        "0","1","2","3","4","5"
    ]

    status = tk.StringVar()
    status.set("0")

    #Catch event
    def treeBatchselect(event):
        row = NewOrderTree_P2.focus()
        if row:
            status.set(NewOrderTree_P2.set(row, 'two'))

    NewOrderTree_P2.bind('<<TreeviewSelect>>', treeBatchselect)

    def set_batch(value):
        row = NewOrderTree_P2.focus()
        if row:
            NewOrderTree_P2.set(row, '1', value)


    dropDownAmountM = ttk.OptionMenu(NewOrderMainPage, status, "0", *AmountList, command=set_batch);
    dropDownAmountM.pack();
    dropDownAmountM.place(x=900, y=490);
    #Change Amount time manual label
    ChangeAmountLabel=Label(NewOrderMainPage, text="Change Amount : ", font=('Helvetica 12'));
    ChangeAmountLabel.pack();
    ChangeAmountLabel.place(x=720,y=490);

    #############################Amount Event over######################

    # ############################Injection Time event#########################
    TimeList = [
        "06:00","06:30","07:00","07:30","08:00","08:30","09:00","09:30","10:00",
    ]

    status = tk.StringVar()
    status.set("00:00")

    #Catch Injection  event
    def InjectionTimeselect(event):
        row = NewOrderTree_P2.focus()
        if row:
            status.set(NewOrderTree_P2.set(row, 'Injection time'))

    NewOrderTree_P2.bind('<<TreeviewSelect>>', InjectionTimeselect)

    def setInjectionTime(value):
        row = NewOrderTree_P2.focus()
        if row:
            NewOrderTree_P2.set(row, '2', value)


    dropDownInjectionT_M = ttk.OptionMenu(NewOrderMainPage, status, "00:00", *TimeList, command=setInjectionTime);
    dropDownInjectionT_M.pack();
    dropDownInjectionT_M.place(x=900, y=460);
    #Change injecion time manual label
    ChangeTImeIjectionLabel=Label(NewOrderMainPage, text="Change Time-Injection : ", font=('Helvetica 12'));
    ChangeTImeIjectionLabel.pack();
    ChangeTImeIjectionLabel.place(x=720,y=460);



    #Create ADD row button+icon

    #by class-option
    # class MyApp(tk.Tk):
    #     def __init__(self, *args, **kwargs,):
    #         tk.Tk.__init__(self, *args, **kwargs)
    #         self.newOrderFrameTemp = tk.Frame(NewOrderMainPage)
    #         self.newOrderFrameTemp.pack()
    #
    #         self.image = tk.PhotoImage(file='./addIcon.png')
    #         self.gmail = tk.Label(self.newOrderFrameTemp, image=self.image)
    #         self.gmail.pack()
    #app = MyApp()

# defining a function that will
# print them on the screen
    #rowTree = StringVar();
    def addRowFunc():
        #global idCounter;
        rowTreetoAdd=(ListofVal[0],ListofVal[1],ListofVal[2]);
        NewOrderTree_P2.insert("", "end", values=rowTreetoAdd);
        ListofVal[0]=ListofVal[0]+1;

    def removeRawFunc():
        #rowTree=rowTree.get();
        #for i,j in zip(range(IntAmount),range(BeginigHour,IntAmount)):
        rawSelectedToDelete=NewOrderTree_P2.selection();
        for rawselected in rawSelectedToDelete:
         NewOrderTree_P2.delete(rawselected);

    #amountVar.set("");

    # Remove button (Icon) - List
    global imgDelete2;
    deleteIcon2 = Image.open("./‏‏deleteIcon.png");
    resizedDeleteIcon2 = deleteIcon2.resize((25,25), Image.ANTIALIAS);
    imgDelete2 = ImageTk.PhotoImage(resizedDeleteIcon2);
    deleteButton2=Button(NewOrderMainPage, image=imgDelete2, borderwidth=0,command=removeRawFunc);
    deleteButton2.pack();
    deleteButton2.place(x=1000, y=98);

    #remove/delete record from db
    # def deleteCyclotronfun():
    #     query = "DELETE FROM resourcecyclotron WHERE idresourceCyclotron = %s"
    #     cyclo_tabel.delete_record(query)


    global addROWImg;
    AddrowLabel=Label(NewOrderMainPage, text="Add row",bg="white", font=('Helvetica 14'));
    AddrowLabel.pack();
    AddrowLabel.place(x=910,y=98);
    #Add row image+button
    AddrowIcon = Image.open("./addIcon.png");
    resized_add_Row = AddrowIcon.resize((25,25), Image.ANTIALIAS);
    addROWImg = ImageTk.PhotoImage(resized_add_Row);
    AddRowButton=Button(NewOrderMainPage,image=addROWImg, borderwidth=0,command=addRowFunc);
    AddRowButton.pack();
    AddRowButton.place(x=880, y=100);




# #############################Batch quantity Event ######################
#
# BatchList = [
#     "0","1","2","3","4","5"
# ]
#
# status = tk.StringVar()
# status.set("0")
#
# #Catch event
# def treeBatchselect(event):
#     row = OrdersTree.focus()
#     if row:
#         status.set(OrdersTree.set(row, 'two'))
#
# OrdersTree.bind('<<TreeviewSelect>>', treeBatchselect)
#
# def set_batch(value):
#     row = OrdersTree.focus()
#     if row:
#         OrdersTree.set(row, '1', value)
#
#
# drop = ttk.OptionMenu(root, status, "0", *BatchList, command=set_batch);
# drop.pack();

#############################Batch Event over######################

# ############################Injection Time event#########################
# TimeList = [
#     "06:00","06:30","07:00","07:30","08:00","08:30"
# ]
#
# status = tk.StringVar()
# status.set("00:00")
#
# #Catch Injection  event
# def InjectionTimeselect(event):
#     row = OrdersTree.focus()
#     if row:
#         status.set(OrdersTree.set(row, 'five'))

#OrdersTree.bind('<<TreeviewSelect>>', InjectionTimeselect)

# def setInjectionTime(value):
#     row = OrdersTree.focus()
#     if row:
#         OrdersTree.set(row, '4', value)
#
#
# drop = ttk.OptionMenu(root, status, "00:00", *TimeList, command=setInjectionTime);
# drop.pack();

############################Injection Time event over#########################




    #NewOrderMainPage.pack(fill='both',expand=1);
    #NewOrderMainPage.mainloop();

#####################end of page number 2 -New order #######################################################################





###########################Oreders main page#################################################
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
#edit field from DB
# query = "UPDATE hospital SET Name = %s ,Fixed_activity_level= %s, Transport_time=%s  WHERE idhospital = %s"
#
# pk = selected_rec[3]
#
# labels = (('Name', ''), ('Fixed activity level', '(mci/h)'),  ('Transport time', '(min)'))
# save_title = "Save Changes"
#
# editHospitalPopup.edit_popup(labels, selected_rec, save_title, query, pk, hospital_tabel)


# Remove button (Icon) - List
deleteIcon = Image.open("./Images/RemoveButton2.png")
resizedDeleteIcon = deleteIcon.resize((105,20), Image.ANTIALIAS)
imgDelete = ImageTk.PhotoImage(resizedDeleteIcon)
deleteButton=Button(ordersFrame, image=imgDelete, borderwidth=0)
deleteButton.pack()
deleteButton.place(x=830, y=65)

#remove/delete record from db
# def deleteCyclotronfun():
#     query = "DELETE FROM resourcecyclotron WHERE idresourceCyclotron = %s"
#     cyclo_tabel.delete_record(query)


#Create New order button
NewOrderIcon = Image.open("./Images/AddnewOrder2.png")
resizedNewOrderIconIcon = NewOrderIcon.resize((120,20), Image.ANTIALIAS)
NewOrderIconimg = ImageTk.PhotoImage(resizedNewOrderIconIcon)
editButton=Button(ordersFrame, image=NewOrderIconimg, borderwidth=0,command=PopUpForNewOrder)
editButton.pack()
editButton.place(x=100, y=65)



root.mainloop();