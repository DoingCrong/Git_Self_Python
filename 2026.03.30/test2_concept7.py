
import numpy as np

import pymysql

conn = pymysql.connect(
    host="localhost", 
    user="root", #사용자
    password="1234", #비밀번호
    database="pythondb", #스키마
    charset="utf8" #한글 깨짐 방지
)

cursor = conn.cursor()

def menu():
    print("1. 성적입력")
    print("2. 전체조회")
    print("3. 1명조회")
    print("4. 성적수정")
    print("5. 성적삭제")
    print("0. 프로그램종료")



student_info = []
student_score = []

while True:
    if __name__ == "__main__":
        menu()

    choice = int(input("입력 : "))

    match choice:
        case 0:
            print("프로그램을 종료합니다.")
            break

        case 1:
            print("\n=== 1. 성적입력 ===")
            while True:
                try:
                    hakbun = int(input("학번 : "))
                    if 0 <= hakbun <= 999999:
                        break
                    else:
                        print("학번은 정수값만 입력하세요.")
                except:
                    print("학번은 정수값만 입력하세요.")
            name = input("이름 : ")
            while True:
                try:
                    kor = int(input("국어: "))
                    if 0 <= kor <= 100:
                        break
                    else:
                        print("점수는 0~100 사이만 입력하세요.")
                except:
                    print("숫자만 입력하세요.")

            while True:
                try:
                    eng = int(input("영어: "))
                    if 0 <= eng <= 100:
                        break
                    else:
                        print("점수는 0~100 사이만 입력하세요.")
                except:
                    print("숫자만 입력하세요.")

            while True:
                try:
                    math = int(input("수학: "))
                    if 0 <= math <= 100:
                        break
                    else:
                        print("점수는 0~100 사이만 입력하세요.")
                except:
                    print("숫자만 입력하세요.")

            student_info.append([hakbun ,name])
            student_score.append([kor, eng, math])

            score = np.array(student_score)

            total = np.sum(score, axis=1)
            average = np.mean(score, axis=1)

            if average>=90:
                grade = "A"
            elif average>=80:
                grade = "B"
            elif average>=70:
                grade = "C"
            elif average>=60:
                grade = "D"
            else: grade = "F"

            
            sql = "insert into student(hakbun, name, kor, eng, math, total, average, grade) values(%s ,%s, %s, %s, %s, %s, %s, %s)" 
            cursor.execute(sql,(hakbun, name, kor, eng, math, total, average, grade))
            conn.commit() #반드시 commit (수정,삭제,삽입에서만)
        
        case 2:
            print("\n=== 2. 전체조회 ===")
            sql = "select * from student"
            cursor.execute(sql) 
            rows = cursor.fetchall()
            for row in rows:
                if row is None:
                    print("전체 데이터가 없습니다.")
                else:
                    print(row)


        case 3:
            sql = "select * from student where hakbun=%s"

            print("\n=== 3. 1명조회 ===")
            while True:
                try:
                    hakbun = int(input("조회할 학번 입력: "))
                    if hakbun == student_info[0]:
                        break
                    else:
                        print("없는 학번입니다.")
                except:
                    print("없는 학번입니다.")
            

            cursor.execute(sql, (hakbun,))

            row = cursor.fetchone()  

            if row is None:
                print("해당 데이터가 없습니다.")
            else:
                print("학번 :", row[0])
                print("이름 :", row[1])
                print("국어 :", row[2])
                print("영어 :", row[3])
                print("수학 :", row[4])
                print("총점 :", row[5])
                print("평균 :", row[6])
                print("학점 :", row[7])

        case 4:
            sql = "update student set kor=%s, eng=%s, math=%s  where hakbun=%s"

            print("\n=== 4. 성적수정 ===")
            while True:
                try:
                    hakbun = int(input("학번 : "))
                    if 0 <= hakbun <= 999999:
                        break
                    else:
                        print("학번은 정수값만 입력하세요.")
                except:
                    print("학번은 정수값만 입력하세요.")
            while True:
                try:
                    kor = int(input("국어: "))
                    if 0 <= kor <= 100:
                        break
                    else:
                        print("점수는 0~100 사이만 입력하세요.")
                except:
                    print("숫자만 입력하세요.")

            while True:
                try:
                    eng = int(input("영어: "))
                    if 0 <= eng <= 100:
                        break
                    else:
                        print("점수는 0~100 사이만 입력하세요.")
                except:
                    print("숫자만 입력하세요.")

            while True:
                try:
                    math = int(input("수학: "))
                    if 0 <= math <= 100:
                        break
                    else:
                        print("점수는 0~100 사이만 입력하세요.")
                except:
                    print("숫자만 입력하세요.")

            cursor.execute(sql, (kor, eng, math, hakbun))
            conn.commit()
                