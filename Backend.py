import mysql.connector

MyDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testtttttt"

)

MyCursor = MyDB.cursor()

MyCursor.execute('CREATE TABLE IF NOT EXISTS Images (id INTEGER(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL)')

def InsertBlob(FilePath):
    with open(FilePath, "rb") as File:
        BinaryData = File.read()
        #(%s) subsituties the value of the variable that u insert  
    SQLStatement = "INSERT INTO Images (Photo) Values (%s)"
    MyCursor.execute(SQLStatement, (BinaryData, )) # Data in the db is paassed as touple
    MyDB.commit()


def RetriveBlob(ID):
    SQLStatement2 = "SELECT * from Images WHERE id = '{0}'"
    MyCursor.execute(SQLStatement2.format(str(ID)))
    MyResult = MyCursor.fetchone()[1] #the id is always touple 
    StoreFilePath = "RetrievedImages/image{0}.jpg".format(str(ID))
    print(MyResult)
    with open(StoreFilePath, "wb") as File:
        File.write(MyResult)
        File.close()
    


print("1. Insert Image \n2. Read Image")
MenuInput = input()

if int(MenuInput) == 1:
    UserFilePath = input("Enter File Path:")
    InsertBlob(UserFilePath)

elif int(MenuInput) == 2:
    UserIDChoice = input("Enter ID:")
    RetriveBlob(UserIDChoice)
