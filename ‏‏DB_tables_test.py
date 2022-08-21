
from ConnectToDB import *   #connect to mysql DB

dbCursor = db.cursor();
#create tables
#Create table of hospitals
dbCursor.execute("CREATE TABLE IF NOT EXISTS hospital ("
                 "idhospital int(255) NOT NULL AUTO_INCREMENT"
                 ",Name varchar(45) NOT NULL"
                 ",Fixed_activity_level float NOT NULL"
                 ",Transport_time_min float NOT NULL"
                 ",Transport_time_max float NOT NULL"
                 ",hospitalcol varchar(45) NOT NULL"
                 ",deleted BOOLEAN DEFAULT FALSE"
                 #"FOREIGN KEY (idhospital) REFERENCES orders(hospitalID),"
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
                 "deleted BOOLEAN DEFAULT FALSE,"
                 "PRIMARY KEY(idresourcemodule))");
#Create table of materials
dbCursor.execute("CREATE TABLE IF NOT EXISTS material("
                 "idmaterial int(255) NOT NULL ,"
                 "materialName varchar(45) not null,"
                 "deleted BOOLEAN DEFAULT FALSE,"
                 "PRIMARY KEY(idmaterial))");

#Create table of workplan
dbCursor.execute("CREATE TABLE IF NOT EXISTS workplan ("
                 "idworkplan int(255) not null"
                 ",Date date not null"
                 ",Cyclotron_activation_time time DEFAULT NULL,"
                 "materialID int(255),"
                 #"orderID int(255) NOT NULL AUTO_INCREMENT,"
                 "PRIMARY KEY(idworkplan),"
                 #"FOREIGN KEY (orderID) REFERENCES orders(idorders),"
                 "FOREIGN KEY (materialID) REFERENCES material(idmaterial))");

#Create table of orders
dbCursor.execute("CREATE TABLE IF NOT EXISTS orders ("
                 "idorders int(255) NOT NULL ,"
                 "DoseNumber int(255) NOT NULL,"
                 "hospitalID int(255) NOT NULL,"
                 "materialID int(255) NOT NULL"
                 ",batchID int(255) AUTO_INCREMENT"
                 ",Date date NOT NULL"
                 ",Injection_time time NOT NULL"
                 ",amount int(255) NOT NULL"
                 ",DecayCorrected float DEFAULT NULL,"
                 "deleted BOOLEAN DEFAULT FALSE,"
                 "updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
                 "PRIMARY KEY(batchID),"
                 "FOREIGN KEY (hospitalID) REFERENCES hospital(idhospital) on update cascade,"
                 "FOREIGN KEY (materialID) REFERENCES material(idmaterial) on update cascade)"
                 # "FOREIGN KEY (batchID) REFERENCES batch(idbatch))"
                 ";");




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
                 "batch_number int(255) DEFAULT NULL,"
                 #"PRIMARY KEY(idbatch) ,"
                 "FOREIGN KEY (idbatch) REFERENCES orders(batchID) on update cascade on delete restrict,"
                 "FOREIGN KEY (resourcecyclotronID) REFERENCES resourcecyclotron(idresourceCyclotron),"
                 "FOREIGN KEY (resourcemoduleID) REFERENCES resourcemodule(idresourcemodule),"
                 "FOREIGN KEY (workplanID) REFERENCES workplan(idworkplan))");



#Data for testing
#Insert data of Hospitals into My-SQl DB
#The INSERT IGNORE statement will cause MySQL to do nothing when the insertion throws an error. If there’s no error, then a new row will be added to the table.
dbCursor.execute("INSERT IGNORE INTO hospital (idhospital,Name,Fixed_activity_level,Transport_time_min,Transport_time_max) VALUES (1,'Belinson',9.2,15.0,20.0),(2,'Ichilov',10.0,20.0,25.0),(3,'Assuta TA',10.9,30.0,35.0),(4,'Sheb',10.5,35.0,40.0),(5,'Ziv',11.0,25.0,30.0),(6,'Assuta Ashdod',13.1,60.0,65.0),(7,'Assaf Harofeh',10.6,65.0,70.0),(8,'Augusta Victoria',9.6,50.0,60.0),(9,'Hila Pharma',9.6,50.0,55.0),(10,'Hadassah',9.5,0.0,0.0);")

#Insert 2 material to the DB,material table
#dbCursor.execute("INSERT IGNORE INTO material (idmaterial,materialName) VALUES (1,'FDG'),(2,'FDOPA');")
#Insert 2 material to the DB,material table
#dbCursor.execute("INSERT IGNORE INTO batch (idbatch) VALUES (1)")


#cleanup DB
db.commit();
dbCursor.close();
