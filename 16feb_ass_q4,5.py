#Q4. What is DQL? Explain SELECT with an example.
# DQL stands for DATA QUERY LANGUAGE . It is used for performing queries on the data within schema objects.

import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="password"
)
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE if not exists test5")    #create the database

#mycursor.execute("CREATE TABLE if not exists test5.test_table(NAME VARCHAR(50) ,MARKS FLOAT ,P_NO INT)")  #create the table

'''mycursor.execute("insert into test5.test_table values('MANIKA' , 45.7 , 2345678)")
mycursor.execute("insert into test5.test_table values('GEETA', 45.9 , 3456899)")        

mydb.commit()'''

mycursor.execute("select NAME from test5.test_table")  

mydb.close()


#Q5. Explain Primary Key and Foreign Key.
'''A primary key generally focuses on the uniqueness of the table. It assures the value in the specific column is unique.
 A foreign key is generally used to build a relationship between the two tables. The table allows only one primary key.'''