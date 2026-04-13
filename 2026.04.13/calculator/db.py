import pymysql

def get_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='1234',
        database='flask_calc_db',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn