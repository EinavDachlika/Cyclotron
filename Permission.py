from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import tkinter as tk
from functools import partial
import sys,importlib
def importAdmin():
    spec = importlib.util.spec_from_file_location("module.name", "D:/PythonProjects/Cyclotron/‏‏settingsTest.py")
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)
    foo.hospital_page()

def importUser():
    spec = importlib.util.spec_from_file_location("module.name", "D:/PythonProjects/Cyclotron/settingsTest1.py")
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)
    foo.hospital_page()




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
        importAdmin();#call to admin pages function
        root.deiconify();
        topPermissionScreen.destroy();

    elif ((UserString == 'user') and (PasswordString == 'user')):
        print("Login successful-User");
        importUser()
        root.deiconify();
        topPermissionScreen.destroy();

    else:
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
username = StringVar();
usernameEntry = Entry(topPermissionScreen, textvariable=username);

#password label and password entry box
passwordLabel = Label(topPermissionScreen,text="Password",font=('Halvetica',10));
password = StringVar()
passwordEntry = Entry(topPermissionScreen, textvariable=password, show='*');

validateLogin = partial(validateLogin, username, password);

#login button
loginButton = Button(topPermissionScreen, text="Login", command=validateLogin);

def LoginButton(event):
    validateLogin();

passwordEntry.bind('<Return>',LoginButton);

CopyrightLabel=Label(topPermissionScreen,text='Copyright to Sheri L.t.d 2022',font=('Arial',8));

Photocanvas.pack();
#TitleLabel.pack;
usernameLabel.pack();
usernameEntry.pack();
passwordLabel.pack();
passwordEntry.pack();
loginButton.pack();
CopyrightLabel.pack();
topPermissionScreen.pack();

#root.withdraw();
root.mainloop();

# if __name__ == '__main__':
#
#     root = tk.Tk()
#     run = Passwordchecker(root)
#     root.mainloop()