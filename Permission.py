from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import tkinter as tk
from functools import partial
import sys,importlib
def importAdmin():
    spec = importlib.util.spec_from_file_location("module.name", "D:\PythonProjects\Cyclotron\‏‏AdminPages.py")
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)
    foo.hospital_page()

def importUser():
    spec = importlib.util.spec_from_file_location("module.name", "D:/PythonProjects/Cyclotron/UserPages.py")
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)
    foo.hospital_page()

def destroy_widget(widget):
    widget.destroy()



def validateLogin(username, password):
#Catch capital letters
    UsersTyped = username.get();
    UserNameList=[];
    for char in UsersTyped:
        k = char.islower()
        if k == True:
            UserNameList.append(char);
        else:
            UserNameList.append(char.lower());


    UserString=''.join(str(element) for element in UserNameList);

#Catch capital letters
    PassTyped=password.get();
    PasswordList=[];
    for char in PassTyped:
        k = char.islower()
        if k == True:
            PasswordList.append(char);
        else:
            PasswordList.append(char.lower());

    PasswordString=''.join(str(element) for element in PasswordList);

    print("username entered :", UserString);
    print("password entered :", PasswordString);

    if ((UserString == 'admin') and (PasswordString == 'sheri')):
        print("Login successful-Admin");
        root.destroy();
        importAdmin();#call to admin pages function
        #root.deiconify();

    elif ((UserString == 'user') and (PasswordString == 'user')):
        print("Login successful-User");
        root.destroy();
        importUser()
        #root.deiconify();

    else:
        CheckInputCheckMsg1=Label(topPermissionScreen, text="Wrong user or password",fg="red",bg="white",font=('Helvetica 9'));
        CheckInputCheckMsg1.pack();
        CheckInputCheckMsg1.place(x=90,y=340);
        root.after(5000, destroy_widget, CheckInputCheckMsg1) ##Clear label after 5 secondes
        CheckInputCheckMsg2=Label(topPermissionScreen, text="Wrong user or password",fg="red",bg="white",font=('Helvetica 9'));
        CheckInputCheckMsg2.pack();
        CheckInputCheckMsg2.place(x=90,y=437);
        root.after(5000, destroy_widget, CheckInputCheckMsg2) ##Clear label after 5 secondes
        print("Wrong password or username");


# def command2():
#     topPermissionScreen.destroy();
#     root.destroy();
#     sys.exit;
#     #window

root = tk.Tk();
#root.title('Main screen');
root.configure(bg='white');
#root.goemtry('800x600');

topPermissionScreen=Frame();

# topPermissionScreen.title(' Login screen ');
# topPermissionScreen.geometry('400x150');
topPermissionScreen.configure(bg='white');


bg=ImageTk.PhotoImage(file="./LogoImage.png");
Photocanvas= Canvas(topPermissionScreen,width=323,height=250);
Photocanvas.create_image(0,0,image=bg,anchor="nw");
Photocanvas.create_text((160,200),text="Sheri Orders System",font=('Halvetica',21))

#username label and text entry box
usernameLabel = Label(topPermissionScreen, text="User Name",font=('Halvetica',10));
usernameLabel.place(x=160,y=150)
username = StringVar();
usernameEntry = Entry(topPermissionScreen, textvariable=username);

#password label and password entry box
passwordLabel = Label(topPermissionScreen,text="Password",font=('Halvetica',10));
password = StringVar()
passwordEntry = Entry(topPermissionScreen, textvariable=password, show='*');

validateLogin = partial(validateLogin, username, password);

#login button
loginButton = Button(topPermissionScreen, text="Login", command=validateLogin);

CancelButton=Button(topPermissionScreen,text="Cancel",command=lambda: [root.destroy()]);
CancelButton.place(x=255,y=461);

def LoginButton(event):
    validateLogin();

passwordEntry.bind('<Return>',LoginButton);

CopyrightLabel=Label(topPermissionScreen,text='Copyright to Sheri L.t.d 2022',font=('Arial',8));

Photocanvas.pack();
#TitleLabel.pack;
usernameLabel.pack(padx=20,pady=20);
usernameEntry.pack();
passwordLabel.pack(padx=20,pady=30);
passwordEntry.pack();
loginButton.pack(padx=10,pady=25);
#CancelButton.pack();
CopyrightLabel.pack();
topPermissionScreen.pack();

#root.withdraw();
root.mainloop();

# if __name__ == '__main__':
#
#     root = tk.Tk()
#     run = Passwordchecker(root)
#     root.mainloop()