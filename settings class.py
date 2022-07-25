from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageFont
import mysql.connector
from mysql.connector import Error
# from importlib import reload

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

def error_message(text):
    messagebox.showerror("Error",text)

def warning_message(text):
    messagebox.showwarning("Warning",text)


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
        else:
            error_message("Please select record")
            self.destroy()



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

    def Add_if_legal(self, Addquery, list,selectMaxIDquery, entries):
        #validation - if al entry box is empty legal= false
        input_values_list = self.get_entry(entries)
        for input_val in input_values_list:
            if input_val=="":
                legal = False
            else:
                legal = True

        if legal:
            try:
                #insert the record to db
                cursor.execute(Addquery, input_values_list)
                db.commit()

                #insert the id from db to values list (not in table) to allow deleting the record without refreshing the page
                cursor.execute(selectMaxIDquery)
                data = cursor.fetchall()
                print(data[0])
                input_values_list.append(data[0][0])
                list.insert(parent='', index='end', iid=None, text='',
                            values=input_values_list)

            except:
                # Rollback in case there is any error
                db.rollback()

        else:
            error_message("There are unallowed empty box. Please fill the empty fiels")
        self.destroy()


    def add_popup(self, labels, save_title, *args):
        # labels and entry box
        p_last_label_x = 30
        p_last_label_y = 80
        value_index=0
        row_num = 1

        # grab record values

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
        self.pack(side=LEFT, padx=lable_place_x + 30, pady=lable_place_y + 50)
        scroll.config(command=self.yview)

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

    def selected_is_non(self, selected_record):
        if selected_record =='':
            text = "Please select a record from the table"
            error_message(text)
            return True
        else:
            return False

    def delete_record(self, query):

        selected_rec = self.selected()
        len = selected_rec.__len__()
        pk_delected_record = selected_rec[len-1]
        pk_delected_record_list = (pk_delected_record, )

        try:
            cursor.execute(query,pk_delected_record_list )
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

        self.delete(self.selection()[0])
#general
label_font = ('Helvetica',26, 'bold')
sub_label_font = ('Helvetica',15, 'bold')
label_color = '#034672'

##################### settings #####################
SettingsFrame = Frame(root)
h = Scrollbar(SettingsFrame, orient='horizontal')
SettingsFrame.pack(fill=X)

# feed label
feedLabel = Label(SettingsFrame, text = 'Settings', font=label_font,fg=label_color)
PlaceLable_X=50
PlaceLable_Y=10

feedLabel.pack(side=LEFT)
feedLabel.place(x=PlaceLable_X,y=PlaceLable_Y)

##################### Cyclotron #####################
# Cyclotron Details label
CyclotronLabel = Label(SettingsFrame, text = 'Cyclotron Details', font=sub_label_font,fg=label_color)
cyclo_Lable_place_x=80
cyclo_Lable_place_y=70

CyclotronLabel.pack(side=LEFT)
CyclotronLabel.place(x=cyclo_Lable_place_x,y=cyclo_Lable_place_y)

###cycortion tabel###
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


###cycortion functions###
def editCyclotronfun():
    selected_rec = cyclo_tabel.selected()
    selected_non=cyclo_tabel.selected_is_non(selected_rec)
    if not selected_non:
        editCyclPopup = Popup()
        editCyclPopup.open_pop('Edit Cyclotron Details')

        query = "UPDATE resourcecyclotron SET version = %s ,capacity= %s, constant_efficiency= %s,description=%s  WHERE idresourceCyclotron = %s"
        # print(cyclo_tabel.focus())
        print(selected_rec)
        pk = selected_rec[4]

        labels = (('Version', ''), ('Capacity', '(mci/h)'), ('Constant Efficiency', '(mCi/mA)'), ('Description', ''))
        save_title = "Save Changes"

        editCyclPopup.edit_popup(labels, selected_rec, save_title, query, pk, cyclo_tabel)


def deleteCyclotronfun():
    query = "DELETE FROM resourcecyclotron WHERE idresourceCyclotron = %s"
    cyclo_tabel.delete_record(query)

def addCyclotronfun():
    addCyclPopup = Popup()
    addCyclPopup.open_pop('Add Cyclotron Details')
    labels = (('Version', ''), ('Capacity', '(mci/h)'), ('Constant Efficiency', '(mCi/mA)'), ('Description', ''))
    save_title = "Add Cyclotron"
    insertquery = "INSERT INTO resourcecyclotron SET version = %s ,capacity= %s, constant_efficiency= %s,description=%s"
    selectIDquery = "SELECT MAX(idresourceCyclotron) FROM resourcecyclotron"
    addCyclPopup.add_popup(labels, save_title, insertquery, cyclo_tabel,selectIDquery)

#cyclotron buttons
#Create a button in the main Window to edit  record (open the popup) - cyclotron
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


# Create a button in the main Window to Delete record - cyclotron
cyclotronDeleteIcon = Image.open("‏‏deleteIcon.png")
resizedCycloDeleteIcon = cyclotronDeleteIcon.resize((20, 20), Image.ANTIALIAS)
imgDeleteCyclotron = ImageTk.PhotoImage(resizedCycloDeleteIcon)
deleteCyclotronButton = Button(SettingsFrame, image=imgDeleteCyclotron, borderwidth=0, command=lambda : deleteCyclotronfun())
deleteCyclotronButton.pack(side=LEFT)
deleteCyclotronButton.place(x=cyclo_Lable_place_x + 500, y=cyclo_Lable_place_y + 15)


##################### Module #####################
# Module Details label
moduleLabel = Label(SettingsFrame, text = 'Module Details', font=sub_label_font,fg=label_color)
module_Lable_place_x=700
module_Lable_place_y=70

moduleLabel.pack(side=RIGHT)
moduleLabel.place(x=module_Lable_place_x,y=module_Lable_place_y)

###module tabel###
scroll_width=20
tab_side=RIGHT
x=1035
y= 160
frame=SettingsFrame
list_height=5
module_tabel_place_x=-30

columns_name_list=('Version', 'Capacity (mci/h)', 'Description')

queryModule = "SELECT * FROM resourcemodule"

module_tabel=table(frame,scroll_width,list_height,tab_side,x,y,module_tabel_place_x,
                   module_Lable_place_y)
module_tabel.create_fully_tabel( columns_name_list, queryModule)

###module functions###
def editModulefun():
    selected_rec = module_tabel.selected()
    selected_non = module_tabel.selected_is_non(selected_rec)
    if not selected_non:
        editModulePopup = Popup()
        editModulePopup.open_pop('Edit Module Details')

        query = "UPDATE resourcemodule SET version = %s ,capacity= %s, description=%s  WHERE idresourcemodule = %s"

        pk = selected_rec[3]

        labels = (('Version', ''), ('Capacity', '(mci/h)'),  ('Description', ''))
        save_title = "Save Changes"

        editModulePopup.edit_popup(labels, selected_rec, save_title, query, pk, module_tabel)


def addModulefun():
    addCyclPopup = Popup()
    addCyclPopup.open_pop('Add Module Details')
    labels = (('Version', ''), ('Capacity', '(mci/h)'), ('Description', ''))
    save_title = "Add Module"
    insetQuery = "INSERT INTO resourcemodule SET version = %s ,capacity= %s,description=%s"
    selectIDquery = "SELECT MAX(idresourcemodule) FROM resourcemodule"
    addCyclPopup.add_popup(labels, save_title, insetQuery, module_tabel,selectIDquery)

def deleteModulefun():
    query = "DELETE FROM resourcecyclotron WHERE idresourcemodule = %s"
    module_tabel.delete_record(query)


#module buttons
#Create a button in the main Window to edit  record (open the popup) - module
moduleEditIcon = Image.open("editIcon.jpg")
resizedModuleEditIcon = moduleEditIcon.resize((20, 20), Image.ANTIALIAS)
imgEditModule = ImageTk.PhotoImage(resizedModuleEditIcon)
editModuleButton = Button(SettingsFrame, image=imgEditModule, borderwidth=0, command=editModulefun)
editModuleButton.pack(side= LEFT)
editModuleButton.place(x=module_Lable_place_x+250, y=module_Lable_place_y+15)


#Create a button in the main Window to Delete record - module
moduleDeleteIcon = Image.open("‏‏deleteIcon.png")
resizedModuleDeleteIcon = moduleDeleteIcon.resize((20, 20), Image.ANTIALIAS)
imgDeleteModule = ImageTk.PhotoImage(resizedModuleDeleteIcon)
deleteModuleButton = Button(SettingsFrame, image=imgDeleteModule, borderwidth=0, command=deleteModulefun)
deleteModuleButton.pack(side= LEFT)
deleteModuleButton.place(x=module_Lable_place_x+300, y=module_Lable_place_y+15)

#Create a button in the main Window to add record - module
moduleAddIcon = Image.open("addIcon.png")
resizedModuleAddIcon = moduleAddIcon.resize((25, 25), Image.ANTIALIAS)
imgAddModule = ImageTk.PhotoImage(resizedModuleAddIcon)
addModuleButton = Button(SettingsFrame, image=imgAddModule, borderwidth=0, command=addModulefun)
addModuleButton.pack(side= LEFT)
addModuleButton.place(x=module_Lable_place_x+200, y=module_Lable_place_y+14)


##################### Hospitals List #####################
hospitalFrame = Frame(root)
hospitalFrame.pack(fill=X)

# hospital label
hospitalLabel = Label(hospitalFrame, text = 'Hospitals Details', font=label_font,fg=label_color)
hospital_Lable_place_x=60
hospital_Lable_place_y=40

hospitalLabel.pack(side=LEFT)
hospitalLabel.place(x=hospital_Lable_place_x,y=hospital_Lable_place_y)

scroll_width=20
tab_side=LEFT
x=650
y= 160
frame=hospitalFrame
list_height=20
c = 80

lable_place_x = 80
lable_place_y=70

columns_name_list=('        Name        ', 'Fixed Activity Level (mci)', 'Transport Time (minutes)')

hospital_query="SELECT * FROM hospital"

hospital_tabel=table(frame,scroll_width,list_height,tab_side,x,y,lable_place_x,
                     lable_place_y)
hospital_tabel.create_fully_tabel( columns_name_list, hospital_query)

hospitalFrame.pack(fill='both',expand=1)

###hospital functions###
def editHospitalfun():
    selected_rec = hospital_tabel.selected()
    selected_non = hospital_tabel.selected_is_non(selected_rec)
    if not selected_non:
        editHospitalPopup = Popup()
        editHospitalPopup.open_pop('Edit Hospital Details')

        query = "UPDATE hospital SET Name = %s ,Fixed_activity_level= %s, Transport_time=%s  WHERE idhospital = %s"

        pk = selected_rec[3]

        labels = (('Name', ''), ('Fixed activity level', '(mci/h)'),  ('Transport time', '(min)'))
        save_title = "Save Changes"

        editHospitalPopup.edit_popup(labels, selected_rec, save_title, query, pk, hospital_tabel)


def addHospitalfun():
    addHospitalPopup = Popup()
    addHospitalPopup.open_pop('Add Hospital Details')
    labels = (('Name', ''), ('Fixed activity level', '(mci/h)'), ('Description', ''))
    save_title = "Add Hospital"
    insetQuery = "INSERT INTO hospital SET Name = %s ,Fixed_activity_level= %s,Transport_time=%s"
    selectIDquery = "SELECT MAX(idhospital) FROM hospital"
    addHospitalPopup.add_popup(labels, save_title, insetQuery, hospital_tabel,selectIDquery)

def deleteHospitalfun():
    query = "DELETE FROM hospital WHERE idhospital = %s"
    hospital_tabel.delete_record(query)


#hospital buttons
#Create a button in the main Window to edit  record (open the popup) - hospital
hospitalEditIcon = Image.open("editIcon.jpg")
resizedHospitalEditIcon = hospitalEditIcon.resize((20, 20), Image.ANTIALIAS)
imgEditHospital = ImageTk.PhotoImage(resizedHospitalEditIcon)
editHospitalButton = Button(hospitalFrame, image=imgEditHospital, borderwidth=0, command= lambda :editHospitalfun())

editHospitalButton.pack(side= LEFT)
editHospitalButton.place(x=lable_place_x+450, y=lable_place_y+15)

#Create a button in the main Window to add record - hospital
hospitalAddIcon = Image.open("addIcon.png")
resizedHospitalAddIcon = hospitalAddIcon.resize((25, 25), Image.ANTIALIAS)
imgAddHospital = ImageTk.PhotoImage(resizedHospitalAddIcon)
addHospitalButton = Button(hospitalFrame, image=imgAddHospital, borderwidth=0, command=lambda : addHospitalfun())
addHospitalButton.pack(side= LEFT)
addHospitalButton.place(x=lable_place_x+400, y=lable_place_y+14)


# Create a button in the main Window to Delete record - hospital
hospitalDeleteIcon = Image.open("‏‏deleteIcon.png")
resizedHospitalDeleteIcon = hospitalDeleteIcon.resize((20, 20), Image.ANTIALIAS)
imgDeleteHospital = ImageTk.PhotoImage(resizedHospitalDeleteIcon)
deleteHospitalButton = Button(hospitalFrame, image=imgDeleteHospital, borderwidth=0, command=lambda : deleteHospitalfun())
deleteHospitalButton.pack(side=LEFT)
deleteHospitalButton.place(x=lable_place_x + 500, y=lable_place_y + 15)


# SettingsFrame.pack()
SettingsFrame.forget()
# hospitalFrame.forget()
root.mainloop()