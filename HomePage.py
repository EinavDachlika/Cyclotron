from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.title("Cyclotron")

#defult font
# root.option_add("*Font", "Helvetica")

# ****** Toolbar ******
class pages(tk.TK):
    def __init__(self, pageName , buttonName):
        self.pageName = pageName
        self.pageFrame = Frame(root, width=300, height=300)

    def toolbar(self):
        # feed label
        feedLabel = Label(self.pageFrame, text=self.pageName, font=('Helvetica', 30, 'bold'), fg='#034672')
        feedLabel.place(x=20, y=30)
        #toolbar
        toolbarbgcolor = "white"
        toolbar = Frame(root, bg=toolbarbgcolor)

        # add logo - toolbar
        LogoImagePath = Image.open("LogoImage.png")
        LogoImageResize = LogoImagePath.resize((120, 57), Image.ANTIALIAS)
        LogoImage = ImageTk.PhotoImage(LogoImageResize)
        Label(toolbar, image=LogoImage).pack(side=LEFT, padx=10, pady=6)

        # work plan button - toolbar
        workPlanButton = Button(toolbar, text="Work Plans", font='Helvetica 11')
        workPlanButton.pack(side=LEFT, padx=10, pady=3)
        # Hospitals button - toolbar
        hospitalsButton = Button(toolbar, text="Hospitals", font='Helvetica 11', bg="#B8CAD7")
        hospitalsButton.pack(side=LEFT, padx=10, pady=3)

        # Orders button - toolbar
        ordersButton = Button(toolbar, text="Orders", font='Helvetica 11')
        ordersButton.pack(side=LEFT, padx=10, pady=3)

        # Reports button - toolbar
        reportsButton = Button(toolbar, text="Reports", font='Helvetica 11')
        reportsButton.pack(side=LEFT, padx=10, pady=3)

        # settings Icon - toolbar

        settingsIcon = Image.open("gearIcon.png")
        resizedSettingsIcon = settingsIcon.resize((35, 35), Image.ANTIALIAS)
        imgSettings = ImageTk.PhotoImage(resizedSettingsIcon)
        Button(toolbar, image=imgSettings, borderwidth=0).pack(side=RIGHT, padx=10, pady=3)

        toolbar.pack(side=TOP, fill=X)

        toolbar.grid_columnconfigure(1, weight=1)


        self.pageFrame.pack(fill="both", expand=True)

        def BoldButton(self):
            listButtons = ["Work Plans", "Hospitals", "Orders","Reports" ]
            for button in listButtons:
                if button == buttonName:
                    styleButton = "Helvetica 12 bold"
                    #BT =


addHospitalPage = pages("Add Hospital")


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

# # Hospitals button - toolbar
# hospitalsButton = Button (toolbar, text="Hospitals",font='Helvetica 12 bold', bg="#B8CAD7")
# hospitalsButton.pack(side=LEFT,padx=10,pady=3)
#
# # Orders button - toolbar
# ordersButton = Button (toolbar, text="Orders", font='Helvetica 11')
# ordersButton.pack(side=LEFT,padx=10,pady=3)
#
#
# # Reports button - toolbar
# reportsButton = Button (toolbar, text="Reports", font='Helvetica 11')
# reportsButton.pack(side=LEFT,padx=10,pady=3)
#
# # settings Icon - toolbar
#
# settingsIcon = Image.open("gearIcon.png")
# resizedSettingsIcon = settingsIcon.resize((35,35), Image.ANTIALIAS)
# imgSettings = ImageTk.PhotoImage(resizedSettingsIcon)
# Button(toolbar, image=imgSettings, borderwidth=0).pack(side=RIGHT,padx=10,pady=3)
#
#
# toolbar.pack(side=TOP, fill=X)
#
# toolbar.grid_columnconfigure(1, weight=1)


#
# toolbarbgcolor = "white smoke"
# toolbar = Frame(root, bg=toolbarbgcolor)
#
# # add logo - toolbar
# LogoImagePath = Image.open("LogoImage.png")
# LogoImageResize = LogoImagePath.resize((120, 57),Image.ANTIALIAS)
# LogoImage = ImageTk.PhotoImage(LogoImageResize)
# Label(toolbar,image=LogoImage).pack(side=LEFT,padx=10,pady=6)
#
# # work plan button - toolbar
# workPlanButton = Button(toolbar, text="Work Plan",font='Helvetica 11')
# workPlanButton.pack(side=LEFT,padx=10,pady=3)
#
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
#
# # Hospitals button - toolbar
# hospitalsButton = Button (toolbar, text="Hospitals")
# hospitalsButton.pack(side=LEFT,padx=10,pady=3)
#
# # Orders button - toolbar
# ordersButton = Button (toolbar, text="Orders", font='Helvetica 12 bold')
# ordersButton.pack(side=LEFT,padx=10,pady=3)
#
#
# # Reports button - toolbar
# reportsButton = Button (toolbar, text="Reports", font='Helvetica 11')
# reportsButton.pack(side=LEFT,padx=10,pady=3)
#
# # settings Icon - toolbar
#
# settingsIcon = Image.open("gearIcon.png")
# resizedSettingsIcon = settingsIcon.resize((35,35), Image.ANTIALIAS)
# imgSettings = ImageTk.PhotoImage(resizedSettingsIcon)
# Button(toolbar, image=imgSettings, borderwidth=0).pack(side=RIGHT,padx=10,pady=3)
#
#
# toolbar.pack(side=TOP, fill=X)
#
# toolbar.grid_columnconfigure(1, weight=1)

root.mainloop()