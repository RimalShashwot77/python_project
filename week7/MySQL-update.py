# import Library
import mysql.connector
import sys
sql = """UPDATE persons set name='Pramish',address='Kathmandu' WHERE pid=5"""
try:
    # Connect with database
    conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
    # Update Record
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    # Close Connection
    cursor.close()
    conn.close()
    print("Update Record successfully")
except:
    print("Error : ", sys.exc_info())  # Display error message