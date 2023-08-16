#Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)


  ''' A cursor in SQL is a database object stored in temp memory and used to work with datasets. 
  A cursor is an object which helps to execute the query and fetch the records from the database. Cursor actually points to results.
  EXECUTE method executes the query.'''

 # Q7. Give the order of execution of SQL clauses in an SQL query.
'''FROM	 
WHERE	
GROUP BY	
HAVING	
SELECT	
ORDER BY	
LIMIT '''
