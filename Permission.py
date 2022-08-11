from tkinter import *
from tkinter import ttk,messagebox
import tkinter as tk
from functools import partial
import sys

def validateLogin(username, password):
    print("username entered :", username.get())
    print("password entered :", password.get())
    return

def command1(event):

    print("username entered :", usernameEntry.get());
    print("password entered :", passwordEntry.get() );

    if ((usernameEntry.get()== 'admin') and (passwordEntry.get() == 'sheri')):
        root.deiconify()
        topPermissionScreen.detroy()
    else:
        print("Wrong passsword or username");


def command2():
    topPermissionScreen.destroy();
    root.destroy();
    sys.exit;
    #window

root = tk.Tk();
#root.title('Main screen');
root.configure(bg='white');
#root.goemtry('800x600');

topPermissionScreen=Frame();

# topPermissionScreen.title(' Login screen ');
# topPermissionScreen.geometry('400x150');
topPermissionScreen.configure(bg='white');

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

passwordEntry.bind('<Return>',command1);
CopyrightLabel=Label(topPermissionScreen,text='Copyright to Sheri L.t.d 2022',font=('Arial',8));

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