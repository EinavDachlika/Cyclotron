from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

LARGE_FONT = ("Helvetica", 14 ,"bold")

class MainFrame(tk.Tk): #inheritance attributes of another class(from TK)
    def __init__(self, *args, **kwargs):
        #args - (arguments) unlimited variables
        #kwargs - (keyword) like a dictionary

        tk.Tk.__init__(self, *args, **kwargs)
        toolbarbgcolor = "white"
        container = tk.Frame(self,bg=toolbarbgcolor)

        # add logo - toolbar
        LogoImagePath = Image.open("LogoImage.png")
        LogoImageResize = LogoImagePath.resize((120, 57), Image.ANTIALIAS)
        LogoImage = ImageTk.PhotoImage(LogoImageResize)
        Label(container, image=LogoImage).pack(side=LEFT, padx=10, pady=6)

        # work plan button - toolbar
        workPlanButton = Button(container, text="Work Plans", font='Helvetica 11')
        workPlanButton.pack(side=LEFT, padx=10, pady=3)
        # Hospitals button - toolbar
        hospitalsButton = Button(container, text="Hospitals", font='Helvetica 11')
        hospitalsButton.pack(side=LEFT, padx=10, pady=3)

        # Orders button - toolbar
        ordersButton = Button(container, text="Orders", font='Helvetica 11')
        ordersButton.pack(side=LEFT, padx=10, pady=3)

        # Reports button - toolbar
        reportsButton = Button(container, text="Reports", font='Helvetica 11')
        reportsButton.pack(side=LEFT, padx=10, pady=3)

        # settings Icon - toolbar

        settingsIcon = Image.open("gearIcon.png")
        resizedSettingsIcon = settingsIcon.resize((35, 35), Image.ANTIALIAS)
        imgSettings = ImageTk.PhotoImage(resizedSettingsIcon)
        Button(container, image=imgSettings, borderwidth=0).pack(side=RIGHT, padx=10, pady=3)

        container.pack(side=TOP, fill=X)

        # container.grid_columnconfigure(1, weight=1)
        # container.pack(side="top", fill="both", expand=True)

        # container.grid_rowconfigure(0, weight=1) #0 is the minimum size, weight is the priority
        # container.grid_columnconfigure(0, weight=1) #0 is the minimum size, weight is the priority


        self.frames = {}

        frame = AddHospitalPage(container, self)

        self.frames[AddHospitalPage] = frame

         # frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(AddHospitalPage)

    def show_frame(self,cont):
        frame = self.frames[cont] #cont is the key
        frame.tkraise() #raise the frame to the front

class createPageWithToolBar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)  #parent is the parent class (it 'MainFrame' class)
        # label = tk.Label(self, text="Start Page", font= LARGE_FONT )
        # label.pack(pady = 10, padx=10)
        # toolbarbgcolor = "white"
        # toolbar = tk.Frame(self, bg=toolbarbgcolor)
        # toolbar.grid(sticky='nesw')
        #
        # # add logo - toolbar
        # LogoImagePath = Image.open("LogoImage.png")
        # LogoImageResize = LogoImagePath.resize((120, 57), Image.ANTIALIAS)
        # LogoImage = ImageTk.PhotoImage(LogoImageResize)
        # Label(toolbar, image=LogoImage).pack(side=LEFT, padx=10, pady=6)
        #
        # # work plan button - toolbar
        # workPlanButton = Button(toolbar, text="Work Plans", font='Helvetica 11')
        # workPlanButton.pack(side=LEFT, padx=10, pady=3)
        # # Hospitals button - toolbar
        # hospitalsButton = Button(toolbar, text="Hospitals", font='Helvetica 11')
        # hospitalsButton.pack(side=LEFT, padx=10, pady=3)
        #
        # # Orders button - toolbar
        # ordersButton = Button(toolbar, text="Orders", font='Helvetica 11')
        # ordersButton.pack(side=LEFT, padx=10, pady=3)
        #
        # # Reports button - toolbar
        # reportsButton = Button(toolbar, text="Reports", font='Helvetica 11')
        # reportsButton.pack(side=LEFT, padx=10, pady=3)
        #
        # # settings Icon - toolbar
        #
        # settingsIcon = Image.open("gearIcon.png")
        # resizedSettingsIcon = settingsIcon.resize((35, 35), Image.ANTIALIAS)
        # imgSettings = ImageTk.PhotoImage(resizedSettingsIcon)
        # Button(toolbar, image=imgSettings, borderwidth=0).pack(side=RIGHT, padx=10, pady=3)
        #
        # toolbar.pack(side=TOP, fill=X)
        #
        # toolbar.grid_columnconfigure(1, weight=1)

class AddHospitalPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font= LARGE_FONT )
        label.pack(fill="both")

        # self.title("Add Hospital")

        # # feed label
        # feedLabel = Label(controller, text='Add Hospital', font=('Helvetica', 30, 'bold'), fg='#034672')
        # feedLabel.place(x=20, y=30)


app = MainFrame()
app.mainloop()