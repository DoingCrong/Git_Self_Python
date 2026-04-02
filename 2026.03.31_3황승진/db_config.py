import pymysql

def db_connect():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="household_db",
        charset="utf8"
    )
    return conn