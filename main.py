
import sys,importlib
import Permission

def importAdmin():
    spec = importlib.util.spec_from_file_location("module.name", "D:\PythonProjects\Cyclotron\‏‏AdminPages.py")
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)

def importUser():
    spec = importlib.util.spec_from_file_location("module.name", "D:/PythonProjects/Cyclotron/UserPages.py")
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)

if ((Permission.user_verified) and (Permission.password_verfied) and (Permission.ValidateTypeOfUser=='admin')):
    print("Login successful-Admin");
    #root.destroy();
    importAdmin();#call to admin pages function
    #root.deiconify();

elif ((Permission.user_verified) and (Permission.password_verfied) and (Permission.ValidateTypeOfUser=='user')):
    print("Login successful-User");
    importUser();
    #root.destroy();
    #importUser();
    #root.deiconify();

