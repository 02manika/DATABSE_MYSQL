#Q3. What is DML? Explain INSERT, UPDATE, and DELETE with an example.
#DML refers to DATA MANIPULATION LANGUAGE , which includes operations like insert , update and delete data in a database .

import mysql.connector
mydb = mysql.connector.connect(
     host = "localhost",
     user = "abc",
     password = "password"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE if not exists test4")

#mycursor.execute("CREATE TABLE if not exists test4.test_table(R_NO INT ,NAME VARCHAR(50) ,MARKS FLOAT ,P_NO INT)")

#mycursor.execute("INSERT INTO test4.test_table (NAME) VALUES ('MANIKA')")     insert command insert the values in the table 

#mycursor.execute("UPDATE test4.test_table SET MARKS = 50 where NAME = 'MANIKA' ")      update command updates the value of an field 

mycursor.execute("DELETE FROM test4.test_table WHERE MARKS = 50")

mydb.close()