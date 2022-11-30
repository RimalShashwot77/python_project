# install library to connect
# https://pypi.org/ # global python library
# pip install mysql-connector-python

# Connect with Database Server
import mysql.connector # import Library
import sys
try:
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'level4d'
    ) # Connect with mysql server
    conn.close() # Connection close with mysql
    print("Connect with database server successfully")
except:
    print("Error", sys.exc_info()) # Display the types of errors