# import Library
import sys
import mysql.connector
sql ="""INSERT INTO persons VALUES(1,'Shashwot',.'Kathmandu')"""
try:
    # Connect
    conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')

    # Insert
    cursor = conn.cursor() # Traveller
    cursor.execute(sql) # insert
    conn.commit() # Save

    # Close
    cursor.close()
    conn.close()
    print("Insert record successfully")
except:
    print("Error : ",sys.exc_info()) # Display error message