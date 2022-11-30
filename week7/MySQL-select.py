# import Library
import mysql.connector
import sys
sql = """SELECT * FROM persons"""
try:
    # connect
    conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d')
    cursor = conn.cursor()
    cursor.execute(sql)
    records = cursor.fetchall()
    print(records)
    # close
    cursor.close()
    conn.close()
    print("Record retrieve successfully")
except:
    print("Error : ",sys.exc_info())