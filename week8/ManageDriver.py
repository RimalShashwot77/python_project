import mysql.connector
import sys
from driver import Driver

def saveDriver(driverInfo):
    conn = None
    sql = """INSERT INTO drivers VALUES (%s, %s, %s)"""
    values = driverInfo.getDID(), driverInfo.getName(), driverInfo.getLicenceNo()
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='level4d'
        )
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("Save driver!")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn

def searchDriver(did):
    pass
def editDriver(driverInfo):
    pass
def deleteDriver(did):
    pass
def allDriver():
    pass
