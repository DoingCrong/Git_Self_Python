import pymysql

def db_connect():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="flasklogindb",
        charset="utf8",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn