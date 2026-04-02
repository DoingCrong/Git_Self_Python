import pymysql

def db_connect():
    conn = pymysql.connect(
        host="localhost",
        user="root",          # 본인 MySQL 계정
        password="1234",      # 본인 MySQL 비밀번호
        database="pythonbankdb",  # 사용할 데이터베이스명
        charset="utf8"
    )
    return conn