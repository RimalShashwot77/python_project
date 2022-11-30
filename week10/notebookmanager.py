import sys
import mysql.connector

def connect():
    conn = None
    try:
        conn = mysql.connector.connect( host='localhost', port='3306', user='root', password='', database='level4d')
    except:
        print("Error: ", sys.exc_info())
    finally:
        return conn

def insert(notebook):
    conn = None
    sql = """INSERT INTO notebook VALUES(%s, %s, %s)"""
    values = (notebook.getNID(), notebook.getPages(), notebook.getPrice())
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result =True
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return result

def all():
    pass

def search(nid):
    sql = """SELECT * FROM notebook WHERE nid=%s"""
    values = (nid, )
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql,values)
        record = cursor.fetchone()
        cursor.close()
        conn.close()
    except:
        print("Error : ",sys.exc_info())
    finally:
        del values
        del conn
        return record

def edit(notebook):
    sql = """UPDATE notebook set pages=%s, price=%s WHERE nid=%s"""
    values = (notebook.getPages(), notebook.getPrice(), notebook.getNID())
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error : ",sys.exc_info())
    finally:
        del values
        del sql
        return result

def delete(nid):
    sql = """DELETE from notebook WHERE nid=%s"""
    values = (nid, )
    result = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        return result