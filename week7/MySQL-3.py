import mysql.connector
import sys

def insertRecord(userInfo):
    conn = None
    sql = """INSERT INTO users values (%s, %s, %s, %s, %s, %s) """
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d',port = '3306')
        cursor = conn.cursor()
        cursor.execute(sql,userInfo)
        conn.commit() # save, update ,delete
        conn.close()
        cursor.close()
        print("User Inserted")
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        del conn

def loginUser(userInfo):
    conn = None
    sql = """SELECT * FROM users WHERE email = %s and password = %s"""
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='level4d',port='3306')
        cursor = conn.cursor()
        cursor.execute(sql,userInfo)
        user = cursor.fetchall()
        print(user)
        if user!=None:
            print('Welcome',user[0][1])
        else:
            print("User Not Found!")
        cursor.close()
        conn.close()
    except:
        print("Error : ", sys.exc_info())
    finally:
        del sql
        del conn

# Test
userInfo = (1, 'Shyam Shrestha', 'Kathmandu', 'shyam@gmail.com', '12345', '9856473245')
# insertRecord(userInfo)
userInfo = ('shyam@gmail.com', '12345')
loginUser(userInfo)