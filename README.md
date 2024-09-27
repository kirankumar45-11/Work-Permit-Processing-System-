# Work-Permit-Processing-System-
 This Python script connects to a MySQL database and manages a permit table. It defines:  Permit Class: Represents a permit with permit_id, employee_name, employer_id, and status. Employer Class: Provides methods to: Create a database (MyDB) Create a table (MyTable) Insert, update, and delete permit records.

MySQL Permit and Employer Database Manager
This Python script connects to a MySQL database to manage permit data. It defines two classes: Permit and Employer. The Employer class includes methods to create a database, table, and perform CRUD operations.

Requirements
Python 3.x
MySQL Server
mysql-connector-python library (pip install mysql-connector-python)
Installation:
pip install mysql-connector-python

Ensure MySQL is running locally with user root and password root.
Usage
Permit Class
Represents a permit with the following attributes:

permit_id
employee_name
employer_id
status (default: "Pending")

Employer Class
Methods:

createdb(): Creates MyDB database.
useDB(): Selects MyDB database.
createProgram(): Creates MyTable to store permit data.
insertProgram(): Inserts a permit record.
updateProgram(): Updates the status of a permit.
deleteProgram(): Deletes a permit record.

e1 = Employer
e1.useDB()
e1.createProgram()
e1.insertProgram()
e1.updateProgram()
e1.deleteProgram()
