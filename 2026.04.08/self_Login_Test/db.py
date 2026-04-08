import pymysql #파이썬에서 제공하는 mysql

# 1번방법
def get_connection():
    return pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="self_flasklogindb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
    #pymysql.cursors.DictCursor : 이제 모든 구문에 db정보를(값) 땡겨올때 사용
    )
