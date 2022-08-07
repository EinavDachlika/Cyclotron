import mysql.connector
from mysql.connector import Error

# connect to MySqL
try:
    #Maor local DB Mysql
    db = mysql.connector.connect(
        host="localhost",
        port=3308,
        user="root",
        password="root",
        database="cyclotron")

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

#create tables
#Create table of hospitals
dbCursor.execute("CREATE TABLE IF NOT EXISTS hospital ("
                 "idhospital int(255) NOT NULL AUTO_INCREMENT"
                 ",Name varchar(45) NOT NULL"
                 ",Fixed_activity_level float NOT NULL"
                 ",Transport_time float NOT NULL"
                 ",hospitalcol varchar(45) NOT NULL"
                 ",deleted BOOLEAN DEFAULT FALSE"
                 ",PRIMARY KEY(idhospital))");

#Create table of resourcecyclotron
dbCursor.execute("CREATE TABLE IF NOT EXISTS resourcecyclotron ("
                 "idresourceCyclotron int(255) NOT NULL AUTO_INCREMENT"
                 ",version varchar(45) not null"
                 ",capacity int(255) not null"
                 ",constant_efficiency int(255) not null,"
                 "description varchar(45) DEFAULT null,"
                 "deleted BOOLEAN DEFAULT FALSE,"
                 "PRIMARY KEY(idresourceCyclotron))");

#Create table of resourcemoule
dbCursor.execute("CREATE TABLE IF NOT EXISTS resourcemodule ("
                 "idresourcemodule int(255) NOT NULL AUTO_INCREMENT"
                 ",version varchar(45) not null"
                 ",capacity int(255) default null,"
                 "description varchar(45) not null,"
                 "deleted BOOLEAN DEFAULT FALSE,"
                 "PRIMARY KEY(idresourcemodule))");
#Create table of materials
dbCursor.execute("CREATE TABLE IF NOT EXISTS material("
                 "idmaterial int(255) NOT NULL AUTO_INCREMENT,"
                 "materialName varchar(45) not null,"
                 "PRIMARY KEY(idmaterial))");

#Create table of workplan
dbCursor.execute("CREATE TABLE IF NOT EXISTS workplan ("
                 "idworkplan int(255) not null"
                 ",Date date not null"
                 ",Cyclotron_activation_time time DEFAULT NULL,"
                 "materialID int(255),"
                 "PRIMARY KEY(idworkplan),"
                 "FOREIGN KEY (materialID) REFERENCES material(idmaterial))");

#Create table of batches
dbCursor.execute("CREATE TABLE IF NOT EXISTS batch("
                 "idbatch int(255) "
                 ",Total_eos_date date"
                 ",Time_leaves_Hadassah_time date,"
                 "Production_site varchar(45),"
                 "batchcol int(255),"
                 "resourcecyclotronID int(255) DEFAULT NULL,"
                 "resourcemoduleID int(255),"
                 "workplanID int(255) DEFAULT NULL,"
                 "TargetCurrentLB int(255) DEFAULT NULL,"
                 "DecayCorrected_TTA int(255) DEFAULT NULL,"
                 "EOS_activity int(255) DEFAULT NULL,"
                 "SynthesisTime int(255) DEFAULT NULL,"
                 "Radioactivity_to_cyclotron int(255),"
                 "PRIMARY KEY(idbatch) ,"
                 "FOREIGN KEY (resourcecyclotronID) REFERENCES resourcecyclotron(idresourceCyclotron),"
                 "FOREIGN KEY (resourcemoduleID) REFERENCES resourcemodule(idresourcemodule),"
                 "FOREIGN KEY (workplanID) REFERENCES workplan(idworkplan))");


#Create table of orders
dbCursor.execute("CREATE TABLE IF NOT EXISTS orders ("
                 "idorders int(255) NOT NULL AUTO_INCREMENT,"
                 "DoseNumber int(255) NOT NULL,"
                 "hospitalID int(255) NOT NULL,"
                 "materialID int(255) NOT NULL"
                 ",batchID int(255) "
                 ",Date date NOT NULL"
                 ",Injection_time time NOT NULL"
                 ",amount int(255) NOT NULL"
                 ",DecayCorrected float DEFAULT NULL,"
                 "PRIMARY KEY(idorders),"
                 "FOREIGN KEY (hospitalID) REFERENCES hospital(idhospital),"
                 "FOREIGN KEY (materialID) REFERENCES material(idmaterial),"
                 "FOREIGN KEY (batchID) REFERENCES batch(idbatch))");

