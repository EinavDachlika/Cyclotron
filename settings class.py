from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageFont
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

cursor = db.cursor()
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
h = Scrollbar(SettingsFrame, orient='horizontal')
SettingsFrame.pack(fill=X)


# feed label
feedLabel = Label(SettingsFrame, text = 'Settings', font=('Helvetica',26, 'bold'),fg='#034672')
PlaceLable_X=50
PlaceLable_Y=10

feedLabel.pack(side=LEFT)
feedLabel.place(x=PlaceLable_X,y=PlaceLable_Y)

##################### Cyclotron #####################
# Cyclotron Details label
CyclotronLabel = Label(SettingsFrame, text = 'Cyclotron Details', font=('Helvetica',15, 'bold'),fg='#034672')
cyclo_Lable_place_x=80
cyclo_Lable_place_y=70

CyclotronLabel.pack(side=LEFT)
CyclotronLabel.place(x=cyclo_Lable_place_x,y=cyclo_Lable_place_y)


class Popup(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        # self.popup = self

    def open_pop(self, title):
        self.geometry("900x550")
        self.title(title)
        Label(self, text=title, font=('Helvetica 17 bold'), fg='#034672').place(x=10, y=18)


        ## in line
        # #labels and entry box
        # p_last_label_x=20
        # p_last_label_y=80
        # i=0
        # column_num=1
        #
        # for lab in labels:
        #     p_label = Label(self, text=lab[0])
        #     p_label.grid(row=1, column=column_num)
        #     p_label.place(x=p_last_label_x, y=p_last_label_y)
        #
        #     # Entry boxes
        #     entry_box = Entry(self, width=15)
        #     entry_box.grid(row=2, column=column_num)
        #     entry_box.place(x=p_last_label_x + 3, y=p_last_label_y + 40)
        #
        #
        #     column_num+=1
        #     if lab[1]!= '':
        #         p_label_units = Label(self, text=lab[1])
        #         font = ("Courier", 9)
        #         p_label_units.config(font=("Courier", 9))
        #         p_label_units_x = p_last_label_x + p_label.winfo_reqwidth()-3
        #         p_label_units.place(x=p_label_units_x, y=p_last_label_y + 7)
        #
        #         if entry_box.winfo_reqwidth() > p_label.winfo_reqwidth()+p_label_units.winfo_reqwidth():
        #             p_last_label_x += entry_box.winfo_reqwidth() + 30
        #         else:
        #             p_last_label_x += p_label.winfo_reqwidth()  +p_label_units.winfo_reqwidth()+ 30
        #     else:
        #         p_last_label_x += entry_box.winfo_reqwidth() + 30


    def update_record(self,query, pk,list, update_values_list):
        selected = list.focus()
        #show the changes
        list.item(selected, text="", values = update_values_list)

        #save new values in the db
        updateCyclotronInDB = query

        try:
            cursor.execute(updateCyclotronInDB, update_values_list)
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        self.destroy()


    def cancel_popup(self):
        self.destroy()


    def save_cancel_button(self, save_title,on_click_save_fun, *args):

        save_button = Button(self, text=save_title,
                               command=lambda: on_click_save_fun(*args))

        save_button.pack(side=LEFT)
        save_button_position_x = self.winfo_screenheight() / 2 - save_button.winfo_reqwidth()/2
        save_button_position_y = 450

        save_button.place(x=save_button_position_x, y=save_button_position_y)

        cancel_button = Button(self, text="Cancle", command=lambda: self.cancel_popup())
        cancel_button.pack(side=LEFT)
        cancel_button.place(x=save_button.winfo_reqwidth() + save_button_position_x + 10, y=save_button_position_y)

    def update_if_clicked(self,query,pk,list,entries):
        update_values_list=self.get_entry(entries)
        update_values_list.append(pk)
        if update_values_list is not None:
            self.update_record(query, pk,list,update_values_list)



    def get_entry(self, entries): # to edit_popup - get user changes in entry box
        update_values_list=[]

        for entry in entries:
            update_values_list.append(entry.get())
        return update_values_list

    # def edit_popup(self, labels,valueList, save_title, query,pk,list)



    def edit_popup(self, labels, valueList, save_title, *args):
        # labels and entry box
        p_last_label_x = 30
        p_last_label_y = 80
        value_index = 0
        row_num = 1

        # grab record values

        # temp_label.config(text=selected)
        entries = []
        for lab in labels:
            p_label = Label(self, text=lab[0])
            p_label.grid(row=row_num, column=1)
            p_label.place(x=p_last_label_x, y=p_last_label_y)

            row_num += 1

            # Entry boxes
            entry_box = Entry(self, width=20)
            entry_box.grid(row=row_num, column=2)
            entry_box.place(x=p_last_label_x + 4, y=p_last_label_y + 30)

            # insert value into entry box
            entry_box.insert(0, valueList[value_index])
            value_index += 1
            entries.append(entry_box)

            if lab[1] != '':
                p_label_units = Label(self, text=lab[1])
                font = ("Courier", 9)
                p_label_units.config(font=("Courier", 9))
                p_label_units_x = p_last_label_x + p_label.winfo_reqwidth()
                p_label_units.place(x=p_label_units_x, y=p_last_label_y + 7)

            p_last_label_y += entry_box.winfo_reqheight() + 35 + p_label.winfo_reqheight()
            row_num += 1

        self.save_cancel_button(save_title, self.update_if_clicked, *args, entries)

    def Add_if_legal(self, query, entries):
        legal=True #check if not null
        input_values_list = self.get_entry(entries)
        if legal:
            try:
                cursor.execute(query, input_values_list)
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

            self.destroy()

        else:
            print("elegal input")

    def add_popup(self, labels, save_title, *args):
        # labels and entry box
        p_last_label_x = 30
        p_last_label_y = 80
        value_index=0
        row_num = 1

        # grab record values

        # temp_label.config(text=selected)
        entries = []
        for lab in labels:
            p_label = Label(self, text=lab[0])
            p_label.grid(row=row_num, column=1)
            p_label.place(x=p_last_label_x, y=p_last_label_y)

            row_num += 1


            # Entry boxes
            entry_box = Entry(self, width=20)
            entry_box.grid(row=row_num, column=2)
            entry_box.place(x=p_last_label_x + 4, y=p_last_label_y + 30)
            entries.append( entry_box)

            if lab[1] != '':
                p_label_units = Label(self, text=lab[1])
                font = ("Courier", 9)
                p_label_units.config(font=("Courier", 9))
                p_label_units_x = p_last_label_x + p_label.winfo_reqwidth()
                p_label_units.place(x=p_label_units_x, y=p_last_label_y + 7)

            p_last_label_y += entry_box.winfo_reqheight() + 35 + p_label.winfo_reqheight()
            row_num += 1

        self.save_cancel_button(save_title, self.Add_if_legal,*args, entries ) # will add save.cancel buttons (and click on functions)


class table(ttk.Treeview):
    def  __init__(self,frame,scroll_width,list_height,side,x_crol,y_crol,lable_place_x,
                               lable_place_y):
        self.side = side
        scroll = Scrollbar(frame, orient="vertical", width=scroll_width)
        scroll.pack(side=side)
        scroll.place(x=x_crol, y=y_crol)
        ttk.Treeview.__init__(self,frame, yscrollcommand=scroll.set, height=list_height)
        self.pack(side=self.side, padx=lable_place_x + 30, pady=lable_place_y + 50)


        # list = self.(frame, yscrollcommand=scroll.set, height=list_height)

    # def create_fully_tabel(self,scroll_width,side, x_crol,y_crol, frame, list_height, lable_place_x,lable_place_y, columns_name_list, query):
    def create_fully_tabel(self, columns_name_list, query):

        # scroll = Scrollbar(frame, orient="vertical", width=scroll_width)
        # scroll.pack(side=side)
        # scroll.place(x=x_crol, y=y_crol)
        #
        # list = ttk.Treeview(frame, yscrollcommand=scroll.set, height=list_height)


        self['columns'] = columns_name_list

        self.column("#0", width=0, stretch=NO)
        self.heading("#0", text="", anchor=CENTER)

        i=0
        len_of_col=len(columns_name_list)
        for column_name in columns_name_list:
            # column format
            if i == 0 or i == len_of_col-2:
                width = len(column_name)*6 +30
            else:
                width = len(column_name)*6

            self.column(column_name, anchor=CENTER, width=width)
            # # Create Headings
            self.heading(column_name, text=column_name, anchor=CENTER)

        # add data from db
        # cursor = db.cursor()
        cursor.execute(query)

        data = cursor.fetchall()

        iid=0
        for recorf in data:
            val=[]
            for i in range (0,len_of_col): # plus 1 is for the pk that will not show in the table
                val.append(recorf[i+1])
            val.append(recorf[0])

            self.insert(parent='', index='end', iid=iid, text='',
                       values=val)
            iid +=1

            self.pack()

    def selected(self):
        selected = self.focus()
        selected_record = self.item(selected, 'values')
        return selected_record



scroll_width=20
tab_side=LEFT
x=613
y= 160
frame=SettingsFrame
list_height=5
lable_place_x = 80
lable_place_y=70
columns_name_list=('Version', 'Capacity (mci/h)', 'Constant Efficiency (mCi/mA)', 'Description')

query = "SELECT * FROM resourcecyclotron"

# cyclo_tabel=table(scroll_width,tab_side, x,y,frame,list_height,lable_place_x,lable_place_y, columns_name_list, query )
cyclo_tabel=table(frame,scroll_width,list_height,tab_side,x,y,lable_place_x,
                               lable_place_y,)
cyclo_tabel.create_fully_tabel( columns_name_list, query)
#
# # scrollbar
# Cyclotron_scroll = Scrollbar(SettingsFrame ,orient="vertical",width=20)
# Cyclotron_scroll.pack(side=LEFT)
# Cyclotron_scroll.place(x=613, y= 160)
#
# cyclo_list = ttk.Treeview(SettingsFrame, yscrollcommand=Cyclotron_scroll.set,height=5)
#
# # cyclo_list.pack(side=LEFT, padx=cyclo_Lable_place_x+30, pady=cyclo_Lable_place_y+50)
#
# # Cyclotron_scroll.config(command=cyclo_list.yview)
# # Cyclotron_scroll.config(command=cyclo_list.xview)
#
# # column define
#
# cyclo_list['columns'] = ('Version', 'Capacity (mci/h)', 'Constant Efficiency (mCi/mA)', 'Description')
#
# # column format
# width_Version=90
# width_Capacity=110
# width_Efficiency=185
# width_Description=110
#
# cyclo_list.column("#0", width=0, stretch=NO)
# cyclo_list.column("Version", anchor=CENTER, width=width_Version)
# cyclo_list.column("Capacity (mci/h)", anchor=CENTER, width=width_Capacity)
# cyclo_list.column("Constant Efficiency (mCi/mA)", anchor=CENTER, width=width_Efficiency)
# cyclo_list.column("Description", anchor=CENTER, width=width_Description)
#
# # Create Headings
# cyclo_list.heading("#0", text="", anchor=CENTER)
# cyclo_list.heading("Version", text="Version", anchor=CENTER)
# cyclo_list.heading("Capacity (mci/h)", text="Capacity (mci/h)", anchor=CENTER)
# cyclo_list.heading("Constant Efficiency (mCi/mA)", text="Constant Efficiency (mCi/mA)", anchor=CENTER)
# cyclo_list.heading("Description", text="Description", anchor=CENTER)
#
# # add data from db
# cursor = db.cursor()
# cursor.execute("SELECT * FROM resourcecyclotron")
#
# cyclotrons = cursor.fetchall()
#
# iid=0
# for cyclo in cyclotrons:
#     print(cyclo)
#     cyclo_list.insert(parent='', index='end', iid=iid, text='',
#                values=(cyclo[1], cyclo[2], cyclo[3],cyclo[4], cyclo[0]))
#     iid +=1
#
# cyclo_list.pack()




#
# def no_choise():
#    selected = cyclo_list.focus()
#    if selected is '':
#       print('empty')
#    else:
#       open_popup_cyclotron()
#
# def open_popup_cyclotron():
#    edit_popup= Toplevel(root)
#    edit_popup.geometry("850x400")
#    edit_popup.title("Edit Cyclotron Details")
#    Label(edit_popup, text= "Edit Cyclotron Details", font=('Helvetica 17 bold'), fg='#034672').place(x=10,y=18)
#
#    # labels
#    popup_label_y=80
#    Version = Label(edit_popup, text="Version")
#    Version.grid(row=1, column=1)
#    version_x = 20
#    Version.place(x=version_x, y=popup_label_y)
#
#
#    Capacity = Label(edit_popup, text="Capacity")
#    Capacity_units = Label(edit_popup, text="(mci/h)")
#    Capacity_units.config(font=("Courier", 9))
#    Capacity.grid(row=1, column=2)
#    capacity_x = version_x+Version.winfo_reqwidth()+70
#    Capacity.place(x=capacity_x, y=popup_label_y)
#    capacity_units_x=capacity_x + Capacity.winfo_reqwidth()
#    Capacity_units.place(x=capacity_units_x, y=popup_label_y+7)
#
#
#    Efficiency = Label(edit_popup, text="Constant Efficiency")
#    Efficiency_units = Label(edit_popup, text="(mCi/mA)")
#    Efficiency_units.config(font=("Courier", 9))
#    Efficiency.grid(row=1, column=3)
#    efficiency_x = capacity_units_x + Capacity_units.winfo_reqwidth() + 45
#    Efficiency.place(x=efficiency_x, y=popup_label_y)
#    efficiency_units_x=efficiency_x + Efficiency.winfo_reqwidth()
#    Efficiency_units.place(x=efficiency_units_x, y=popup_label_y+7)
#
#
#    Description = Label(edit_popup, text="Description")
#    Description.grid(row=1, column=3)
#    description_x = efficiency_units_x+ Efficiency_units.winfo_reqwidth() + 20
#    Description.place(x=description_x, y=popup_label_y)
#
#    # Entry boxes
#    Version_entry = Entry(edit_popup, width=10)
#    Version_entry.grid(row=2, column=1)
#    Version_entry.place(x=version_x+3, y=popup_label_y+30)
#
#    Capacity_entry = Entry(edit_popup, width=14)
#    Capacity_entry.grid(row=2, column=2)
#    Capacity_entry.place(x=capacity_x, y=popup_label_y+30)
#
#
#    Efficiency_entry = Entry(edit_popup, width=15)
#    Efficiency_entry.grid(row=2, column=3)
#    Efficiency_entry.place(x=efficiency_x, y=popup_label_y+30)
#
#
#    Description_entry = Entry(edit_popup,width=15)
#    Description_entry.grid(row=2, column=4)
#    Description_entry.place(x=description_x, y=popup_label_y+30)
#
#
#    # # clear entry boxes
#    # Version_entry.delete(0, END)
#    # Capacity_entry.delete(0, END)
#    # Efficiency_entry.delete(0, END)
#
#    # grab record
#    selected = cyclo_list.focus()
#    # grab record values
#    values = cyclo_list.item(selected, 'values')
#    # temp_label.config(text=selected)
#
#    # insert cyclotron details from db to entry boxes
#    Version_entry.insert(0, values[0])
#    Capacity_entry.insert(0, values[1])
#    Efficiency_entry.insert(0, values[2])
#    Description_entry.insert(0,values[3])
#
#    get_old_version = Version_entry.get()
#    # get_capacity = Capacity_entry.get()
#    # get_efficiency = Efficiency_entry.get()
#    # get_description = Description_entry.get()
#
#    select_button = Button(edit_popup, text="Save Changes", command=lambda :update_cyclo_record(edit_popup,get_old_version,Version_entry.get(),Capacity_entry.get(),Efficiency_entry.get(),Description_entry.get()))
#
#    select_button.pack(side=LEFT)
#    select_button_position= edit_popup.winfo_screenheight()/2-select_button.winfo_reqwidth()/2
#    select_button.place(x=select_button_position, y=250)
#
#    cancel_button = Button(edit_popup, text="Cancle", command=lambda :cancel_cyclo_popup(edit_popup))
#    cancel_button.pack(side=LEFT)
#    cancel_button.place(x=select_button.winfo_reqwidth()+select_button_position+10, y=250)
#
#
# def cancel_cyclo_popup(edit_popup):
#    edit_popup.destroy()
#
# def update_cyclo_record(edit_popup,old_version,get_version, get_capacity, get_efficiency, get_description):
#    # print("get_version" + get_version)
#    selected = cyclo_list.focus()
#    # print(cyclo_list.item(selected, 'values'))
#    # save new data
#    cyclo_list.item(selected, text="", values=(get_version, get_capacity, get_efficiency, get_description))
#    print(get_version)
#    updateCyclotronInDB = "UPDATE resourcecyclotron SET version = %s ,capacity= %s, constant_efficiency= %s,description=%s  WHERE version = %s"
#    updateValues = (get_version, get_capacity,get_efficiency,get_description,old_version)
#    try:
#       cursor.execute(updateCyclotronInDB, updateValues )
#       db.commit()
#    except:
#       # Rollback in case there is any error
#       db.rollback()
#
#
#    edit_popup.destroy()
#
#
#
#
def editCyclotronfun():
    selected_rec = cyclo_tabel.selected()
    if  cyclo_tabel.focus() =='':
        print('empty') #message
    else:

        editCyclPopup = Popup()
        editCyclPopup.open_pop('Edit Cyclotron Details')


        query = "UPDATE resourcecyclotron SET version = %s ,capacity= %s, constant_efficiency= %s,description=%s  WHERE idresourceCyclotron = %s"
        # print(cyclo_tabel.focus())
        print(selected_rec)
        pk = selected_rec[4]

        labels = (('Version', ''), ('Capacity', '(mci/h)'), ('Constant Efficiency', '(mCi/mA)'), ('Description', ''))
        save_title = "Save Changes"

        editCyclPopup.edit_popup(labels, selected_rec, save_title, query, pk, cyclo_tabel)

def addCyclotronfun():
        addCyclPopup = Popup()
        addCyclPopup.open_pop('Add Cyclotron Details')
        labels = (('Version', ''), ('Capacity', '(mci/h)'), ('Constant Efficiency', '(mCi/mA)'), ('Description', ''))
        save_title = "Add Cyclotron"
        query = "INSERT INTO resourcecyclotron SET version = %s ,capacity= %s, constant_efficiency= %s,description=%s"

        addCyclPopup.add_popup(labels, save_title, query)


# #Create a button in the main Window to edit  record (open the popup) - cyclotron
cyclotronEditIcon = Image.open("editIcon.jpg")
resizedCycloEditIcon = cyclotronEditIcon.resize((20, 20), Image.ANTIALIAS)
imgEditCyclotron = ImageTk.PhotoImage(resizedCycloEditIcon)
# editCyclotronButton = Button(SettingsFrame, image=imgEditCyclotron, borderwidth=0, command= lambda :editCyclotronfun())
editCyclotronButton = Button(SettingsFrame, image=imgEditCyclotron, borderwidth=0, command= lambda :editCyclotronfun())

editCyclotronButton.pack(side= LEFT)
editCyclotronButton.place(x=cyclo_Lable_place_x+450, y=cyclo_Lable_place_y+15)

#Create a button in the main Window to add record - cyclotron
cyclotronAddIcon = Image.open("addIcon.png")
resizedCycloAddIcon = cyclotronAddIcon.resize((25, 25), Image.ANTIALIAS)
imgAddCyclotron = ImageTk.PhotoImage(resizedCycloAddIcon)
addCyclotronButton = Button(SettingsFrame, image=imgAddCyclotron, borderwidth=0, command=lambda : addCyclotronfun())
addCyclotronButton.pack(side= LEFT)
addCyclotronButton.place(x=cyclo_Lable_place_x+400, y=cyclo_Lable_place_y+14)


SettingsFrame.pack()
root.mainloop()