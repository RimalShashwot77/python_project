# import Library
import mysql.connector
import sys
sql = """DELETE FROM students WHERE, pid=1"""
try:
    # Connect with database
    conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
    # Delete Record
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    # Close Connection
    cursor.close()
    conn.close()
    print("Delete Record successfully")
except:
    print("Error : ", sys.exc_info())  # Display error message