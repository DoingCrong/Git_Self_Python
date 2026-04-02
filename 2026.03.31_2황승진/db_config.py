import pymysql

def db_connect():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="1234",
        database="python_car_loan_db",
        charset="utf8"
    )
    return conn