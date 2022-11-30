# # import library
# import sys
# import mysql.connector
# sql ="""INSERT INTO students VALUES(1,'Shashwot',80,80)"""
# try:
#     # Connect
#     conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
#
#     # Insert
#     cursor = conn.cursor() # Traveller
#     cursor.execute(sql) # insert
#     conn.commit() # Save
#
#     # Close
#     cursor.close()
#     conn.close()
#     print("Insert record successfully")
# except:
#     print("Error : ",sys.exc_info()) # Display error message


import mysql.connector
import sys

def insertRecord():
    try:
       sql ="""INSERT INTO students VALUES(%s, %s, %s, %s)"""
       values = [1,'Gaurav',67,78]
       conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
       cursor = conn.cursor()
       cursor.execute(sql, values)
       conn.commit()
       cursor.close()
       conn.close()
       print("Record Inserted")
    except:
       print("Error : ", sys.exc_info())

def searchRecord():
    try:
       sid = (1,)
       sql = """SELECT * FROM students"""
       conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
       cursor = conn.cursor()
       cursor.execute(sql, sid)
       record = cursor.fetchone()
       print(record)
       cursor.close()
       conn.close()
       print("Successfully Searched")
    except:
        print("Error: ",sys.exc_info())

def displayAll():
    try:
        sql = """SELECT * FROM students"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        print(records)
        conn.commit()
        cursor.close()
        conn.close()
        print("Successfully Displayed")
    except:
        print("Error : ",sys.exc_info())

def updateRecord():
    try:
        values = ('Shashwot',98,69,1)
        sql = """UPDATE students set name = %s, isd = %s, fcs = %s WHERE sid = %s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Record Updated")
    except:
        print("Error: ",sys.exc_info())

def deleteRecord():
    try:
        sid = (1,)
        sql = """DELETE FROM students WHERE sid=%s"""
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
        cursor = conn.cursor()
        cursor.execute(sql, sid)
        conn.commit()
        cursor.close()
        conn.close()
        print("Record Deleted")
    except:
        print("Error: ",sys.exc_info())

# Test
# insertRecord()
# searchRecord()
# displayAll()
# updateRecord()
deleteRecord()

