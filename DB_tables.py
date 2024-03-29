
from ConnectToDB import *   #connect to mysql DB

dbCursor = db.cursor();
#Create Cyclotron DB
dbCursor.execute("CREATE SCHEMA IF NOT EXISTS cyclotron");

#create tables
#Create table of hospitals
dbCursor.execute("CREATE TABLE IF NOT EXISTS hospital ("
                 "idhospital int(255) NOT NULL AUTO_INCREMENT"
                 ",Name varchar(45) NOT NULL"
                 ",Fixed_activity_level float NOT NULL"
                 ",Transport_time_min float NOT NULL"
                 ",Transport_time_max float NOT NULL"
                 ",deleted BOOLEAN DEFAULT null"
                 ",PRIMARY KEY(idhospital))");

#Create table of resourcecyclotron
dbCursor.execute("CREATE TABLE IF NOT EXISTS resourcecyclotron ("
                 "idresourceCyclotron int(255) NOT NULL AUTO_INCREMENT"
                 ",version varchar(45) not null"
                 ",capacity int(255) not null"
                 ",constant_efficiency int(255) not null,"
                 "description varchar(45) DEFAULT null,"
                 "deleted BOOLEAN DEFAULT null,"
                 "PRIMARY KEY(idresourceCyclotron))");

#Create table of hospitals
dbCursor.execute("CREATE TABLE IF NOT EXISTS users ("
                 "iduser int(255) NOT NULL AUTO_INCREMENT"
                 ",Name varchar(45) NOT NULL,"
                 "Password varchar(45) BINARY NOT NULL"#Binari=case senaitive password 
                 ",userType ENUM('admin','user','editor') DEFAULT 'user',"
                 "lastSeen  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"
                 ",PRIMARY KEY(iduser))");


#Create table of resourcemoule
dbCursor.execute("CREATE TABLE IF NOT EXISTS resourcemodule ("
                 "idresourcemodule int(255) NOT NULL AUTO_INCREMENT"
                 ",version varchar(45) not null"
                 ",capacity int(255) default null,"
                 "description varchar(45) not null,"
                 "deleted BOOLEAN DEFAULT null,"
                 "PRIMARY KEY(idresourcemodule))");
#Create table of materials
dbCursor.execute("CREATE TABLE IF NOT EXISTS material("
                 "idmaterial int(255) NOT NULL AUTO_INCREMENT,"
                 "materialName varchar(45) not null,"
                 "deleted BOOLEAN DEFAULT null,"
                 "PRIMARY KEY(idmaterial))");

#Create table of workplan
dbCursor.execute("CREATE TABLE IF NOT EXISTS workplan ("
                 "idworkplan int(255) NOT NULL AUTO_INCREMENT"
                 ",Date date not null,"
                 "materialID int(255) not null"
                 ",Cyclotron_activation_time time DEFAULT NULL,"
                 "deleted VARCHAR(45) DEFAULT NULL,"
                 "PRIMARY KEY(idworkplan),"
                 "FOREIGN KEY (materialID) REFERENCES material(idmaterial))");

#Create table of batches
dbCursor.execute("CREATE TABLE IF NOT EXISTS batch("
                 "idbatch int(255) NOT NULL AUTO_INCREMENT"
                 ",Total_eos int(255) DEFAULT NULL"
                 ",Time_leaves_Hadassah time,"
                 "Production_site varchar(45),"
                 "batchcol int(255),"
                 "resourcecyclotronID int(255) DEFAULT NULL,"
                 "resourcemoduleID int(255),"
                 "workplanID int(255) DEFAULT NULL,"
                 "TargetCurrentLB int(255) DEFAULT NULL,"
                 "DecayCorrected_TTA int(255) DEFAULT NULL,"
                 "EOS_activity int(255) DEFAULT NULL,"
                 "SynthesisTime time DEFAULT NULL,"
                 "Radioactivity_to_cyclotron int(255),"
                 "batchNumber int(255) DEFAULT NULL,"
                 "EOS_TIME time,"
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
                 ",batchID int(255) DEFAULT NULL"
                 ",Date date NOT NULL"
                 ",Injection_time time NOT NULL"
                 ",amount int(255) NOT NULL"
                 ",DecayCorrected float DEFAULT NULL,"
                 "deleted BOOLEAN DEFAULT null,"
                 "updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
                 "PRIMARY KEY(idorders),"
                 "FOREIGN KEY (hospitalID) REFERENCES hospital(idhospital) on update cascade,"
                 "FOREIGN KEY (materialID) REFERENCES material(idmaterial) on update cascade,"
                 "FOREIGN KEY (batchID) REFERENCES batch(idbatch));");


# #Data for testing
# #Insert data of Hospitals into My-SQl DB
# #The INSERT IGNORE statement will cause MySQL to do nothing when the insertion throws an error. If there’s no error, then a new row will be added to the table.
# dbCursor.execute("INSERT IGNORE INTO hospital (idhospital,Name,Fixed_activity_level,Transport_time_min,Transport_time_max) VALUES (1,'Belinson',9.2,15.0,20.0),(2,'Ichilov',10.0,20.0,25.0),(3,'Assuta TA',10.9,30.0,35.0),(4,'Sheb',10.5,35.0,40.0),(5,'Ziv',11.0,25.0,30.0),(6,'Assuta Ashdod',13.1,60.0,65.0),(7,'Assaf Harofeh',10.6,65.0,70.0),(8,'Augusta Victoria',9.6,50.0,60.0),(9,'Hila Pharma',9.6,50.0,55.0),(10,'Hadassah',9.5,0.0,0.0);")
#
# #Insert 2 material to the DB,material table
# dbCursor.execute("INSERT IGNORE INTO material (idmaterial,materialName) VALUES (1,'FDG'),(2,'FDOPA');")
# #cleanup DB
# db.commit();
# dbCursor.close();
