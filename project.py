import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root'
    )

mycursor=mydb.cursor()

# Simulated Database
permit_db = {}
employer_db = {}

# Permit Class to hold information about a permit
class Permit:
    def __init__(self, permit_id, employee_name, employer_id, status="Pending"):
        self.permit_id = permit_id
        self.employee_name = employee_name
        self.employer_id = employer_id
        self.status = status

# Employer Class to hold information about an employer
class Employer:
    
    def createdb():
        try:
            mycursor.execute("CREATE DATABASE MyDB")
        except Exception:
            print('Already Created DB')

    def useDB():
        try:
            mycursor.execute("USE MyDB")
            print('Using MYDB')
        except Exception:
            print('Already Used DB')

    def createProgram():
        try:
            mycursor.execute("CREATE TABLE MyTable (permit_id int(10),employee_name varchar(100),employer_id int(20),status varchar(20))")
            mydb.commit()
            print('created table succesfully')
        except Exception:
            print('Already Created Table')

    def insertProgram():
        try:
            mycursor.execute("INSERT INTO MyTable(permit_id,employee_name,employer_id,status) values('101','Umer',1,'Completed')")
            mydb.commit()
            print('Inserted Successfully!')
        except Exception:
            print('Already Inserted Data into Table')
    def updateProgram():
        try:
            mycursor.execute("UPDATE MyTable set status='pending' where name='Umer' ")
            mydb.commit()
            print('Updated Successfully!')
        except Exception:
            print('Already Inserted Data into Table')
    def deleteProgram():
        try:
            mycursor.execute("delete from MyTable  where name='Umer' ")
            mydb.commit()
            print('Deleted Successfully!')
        except Exception:
            print('Issue while Deleting')

e1=Employer
e1.useDB()
#e1.createProgram()
#e1.insertProgram()
e1.updateProgram()
e1.deleteProgram()
