from tkinter import *
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import tkinter as tk
from functools import partial
import sys,importlib
import mysql.connector
from mysql.connector import Error
from ConnectToDB import *   #connect to mysql DB



# def importAdmin():
#     spec = importlib.util.spec_from_file_location("module.name", "D:\PythonProjects\Cyclotron\‏‏AdminPages.py")
#     foo = importlib.util.module_from_spec(spec)
#     sys.modules["module.name"] = foo
#     spec.loader.exec_module(foo)
#    # foo.hospital_page()
#
# def importUser():
#     spec = importlib.util.spec_from_file_location("module.name", "D:/PythonProjects/Cyclotron/UserPages.py")
#     foo = importlib.util.module_from_spec(spec)
#     sys.modules["module.name"] = foo
#     spec.loader.exec_module(foo)
#    # foo.hospital_page()

def destroy_widget(widget):
    widget.destroy()



def validateLogin(username, password):
    global user_verified,password_verfied,ValidateTypeOfUser;
    UsersTyped = username.get();
    PassTyped=password.get();

    #Catch capital letters
    #UsersTyped = username.get();
    UserNameList=[];
    for char in UsersTyped:
        k = char.islower()
        if k == True:
            UserNameList.append(char);
        else:
            UserNameList.append(char.lower());


    UserString=''.join(str(element) for element in UserNameList);



    cursor = db.cursor();
    GetCredentialsQuery=f"SELECT Name,Password,userType FROM users  WHERE Name='{UserString}' AND Password='{PassTyped}';";
    cursor.execute(GetCredentialsQuery);
    dataFromDb = cursor.fetchall();
    print(dataFromDb);


    if dataFromDb:
        #convert list of tuples into list
        ListOfDataFromDB = [item1 for t1 in dataFromDb for item1 in t1];
        print(ListOfDataFromDB);
        # print("user:",ListOfDataFromDB[0]);
        # print("pass:",ListOfDataFromDB[1]);
        # print("Type od user:",ListOfDataFromDB[2]);
        user_verified=ListOfDataFromDB[0];
        password_verfied=ListOfDataFromDB[1];
        ValidateTypeOfUser=ListOfDataFromDB[2];
        print("Login successful",dataFromDb);

    else:
        messagebox.showerror("Error message","There is no user or password that fit the DB,please try again!");
        raise Exception("There is no user or password contain in DB");

    db.commit();
    cursor.close();


    print("username entered :", user_verified);
    print("password entered :", password_verfied);

    if ((user_verified) and (password_verfied) and (ValidateTypeOfUser=='admin')):
        print("Login successful-Admin");
        root.destroy();
     #   importAdmin();#call to admin pages function
        #root.deiconify();

    elif ((user_verified) and (password_verfied) and (ValidateTypeOfUser=='user')):
        print("Login successful-User");
        root.destroy();
#        importUser()
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

Photocanvas= Canvas(topPermissionScreen,width=400,height=250);
SheriLogoImg=(Image.open("./Images/logoSheri2.png"))
resizedSheriLogoimage= SheriLogoImg.resize((400,250), Image.ANTIALIAS)
ResizedSheriImage=ImageTk.PhotoImage(resizedSheriLogoimage);
Photocanvas.create_image(0,0,image=ResizedSheriImage,anchor="nw");
Photocanvas.create_text((210,147),text="Welcome to \n\nS.R.Y Orders System ",fill="red",font=('Halvetica',30))

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
CancelButton.place(x=315,y=480);

def LoginButton(event):
    validateLogin();

passwordEntry.bind('<Return>',LoginButton);

CopyrightLabel=Label(topPermissionScreen,text='Copyright to S.R.Y L.t.d 2022',font=('Arial',8));

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