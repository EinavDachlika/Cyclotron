
import sys,importlib
import Permission

# def importAdmin():
#     sys.path.append("./UserPages.py")

def importAdmin():
    spec = importlib.util.spec_from_file_location("module.name", r"‏‏AdminPages.py")
    foo = importlib.util.module_from_spec(spec)
    sys.modules["module.name"] = foo
    spec.loader.exec_module(foo)
#foo.importAdmin();#call to admin pages function

# def importUser():
#     spec = importlib.util.spec_from_file_location("module.name", "./UserPages.py")
#     foo = importlib.util.module_from_spec(spec)
#     sys.modules["module.name"] = foo
#     spec.loader.exec_module(foo)

# if ((Permission.user_verified) and (Permission.password_verfied) and (Permission.ValidateTypeOfUser=='admin')):
#     print("Login successful-Admin");
#     #root.destroy();
# importAdmin();#call to admin pages function
    #root.deiconify();

# elif ((Permission.user_verified) and (Permission.password_verfied) and (Permission.ValidateTypeOfUser=='user')):
#     print("Login successful-User");
#     importAdmin();
#     #root.destroy();
#     #importUser();
#     #root.deiconify();
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    importAdmin()

