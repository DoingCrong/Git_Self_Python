import pymysql

conn = pymysql.connect(
    host="localhost", 
    user="root", #사용자
    password="1234", #비밀번호
    database="pythondbtest", #스키마
    charset="utf8" #한글 깨짐 방지
)

# <삽입>
cursor = conn.cursor()
sql = "insert into student(name, kor, eng, math) values(%s, %s, %s, %s)" 
cursor.execute(sql,("홍길동", 90,85,95)) #지정된 변수에 값을 대입?
conn.commit() #반드시 commit (수정,삭제,삽입에서만)

# <전체자료조회>
# sql = "select * from student"
# cursor.execute(sql) #select 구문에서는 실행후 꼭 전체 내용을 가지고 오는 구문을 작성해야 함.
# rows = cursor.fetchall() #조회 전부를 가지고 옴. 
# for row in rows:
#       print(row)

# <업데이트>
# sql = "update student set kor=%s where name=%s"
# cursor.execute(sql, (100, "홍길동"))
# conn.commit()


# <삭제>
# sql = "delete from student where name=%s"
# cursor.execute(sql, ("홍길동",))
# conn.commit()

# <한사람 조회>

sql = "select * from student where name=%s"

name = input("조회할 이름 입력: ")

cursor.execute(sql, (name,))

row = cursor.fetchone()  # 한 개만 가져오기

if row is None:
    print("해당 데이터가 없습니다.")
else:
    print("이름 :", row[0])
    print("국어 :", row[1])
    print("영어 :", row[2])
    print("수학 :", row[3])