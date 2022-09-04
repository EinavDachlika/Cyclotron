import mysql.connector
from mysql.connector import Error

# connect to MySqL
try:
    #SRY local DB Mysql
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database="cyclotron",
        auth_plugin='mysql_native_password'
    )

    #
    # #Maor local DB Mysql
    # db = mysql.connector.connect(
    #     host="localhost",
    #     port=3308,
    #     user="root",
    #     password="root",
    #     database="cyclotron")

    # # # Einav local DB-Mysql
    # db = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     password="Cyclotron2022@?%",
    #     database= "cyclotron")

    if db.is_connected():
        # db_Info = db.get_server_info()
        # print("Connected to MySQL Server version ", db_Info)
        dbCursor = db.cursor(buffered=True)
        # Check to see if connection to Mysql was created
        print("connection to local mysql succeed", db)

# dbCursor.execute("select database();")
# record = dbCursor.fetchone()
# print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
