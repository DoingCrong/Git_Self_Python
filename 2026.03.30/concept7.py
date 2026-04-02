"""
파이썬 object 타입
여러 성격의 자료를 저장 가능(파이썬 리스트와 유사함.)
arr = np.arry([1, "홍길동", 3.5],dype=object)
arr1 = [["홍길동",100,90,100],
        ["이순신", 90,90,90]]
arr2 = np.array(arr1, dtype=object)

타입을 object로 하면 실행속도 느려지고, 계산능력도 떨어짐, 벡터 연산에도 비효육적임.

------------------------------------------------------------------------------------
넘파이 기본연산

수치연산을 진행할때 각각의 타입이 다르면 자동 형변환 가능 작 -> 큰(int < float < complex)

넘파이 집계함수
np.sum() : 모든 요소의 합
np.mean() : 모든 요소의 평균
np.min() : 모든 요소의 최소값
np.max() : 모든 요소의 최대값
np.std() : 표준 편차
np.var() : 분산
np.argmax() : 모든 요소의 최대값의 인덱스(위치)
np.cumsum() : 모든 요소의 누적합

ex)
#pip install numpy

import numpy as np

arr = np.array([10,20,30,40,50])

print("합계 : ", np.sum(arr)) ---> 합계 :  150
print("평균 : ", np.mean(arr)) ---> 평균 :  30.0
print("최대값 : ", np.max(arr)) ---> 최대값 :  50
print("최소값 : ", np.min(arr)) ---> 최소값 :  10
print("표준편차 : ", np.std(arr)) ---> 표준편차 :  14.142135623730951
print("분산 : ", np.var(arr)) ---> 분산 :  200.0
print("최대값 위치 : ", np.argmax(arr)) ---> 최대값 위치 :  4 #인덱스 위치
print("최소값 위치 : ", np.argmin(arr)) ---> 최소값 위치 :  0

import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60]
])

print("열합계 : ", np.sum(arr, axis=0)) ---> 열합계 :  [50 70 90] #axis=0 : 열방향으로(세로)
print("행합계 : ", np.sum(arr, axis=1)) ---> 행합계 :  [ 60 150] #axis=1 : 행방향으로(가로)
print("행평균 : ", np.mean(arr, axis=1)) ---> 행평균 :  [20. 50.]
print("열최대 : ", np.max(arr, axis=0)) ---> 열최대 :  [40 50 60]
print("열최소 : ", np.min(arr, axis=0)) ---> 열최소 :  [10 20 30]


---------------------------------------------------------------------------------------------------------------
===================================================== < Phtyhon > ================================================
---------------------------------------------------------------------------------------------------------------

1. 상속

파이썬 시작 구문

파이썬을 실행하면 처음 실행하고자 하는 구문을 지정 가능 함.
def main():
구문


if __name__ == "__main__":
main() #처음 실행하고자하는 함수 실행.

모든 프로그램은 이런식으로 작성한다. 즉 자바에서 main()정도로 인식.

--------------------------------------------------------------------



파이썬 mysql 연동
종류
mysql-connector-python
pymysql

mysql-connector-python
라이브러리 설치 : pip install connector-python

pymysql
라이브러리 설치 : pip install pymysql

import pymysql
db에 접속하기

1. db접속
conn = pymysql.connect(
    host="localhost", 
    user="root", #사용자
    password="1234", #비밀번호
    database="pythondb", #스키마
    charset="utf8" #한글 깨짐 방지
)


2. 커서생성하기
cursor = conn.cursor() #데이터 베이스와 연동을 할수 있도록 하는 작업(항상 먼제 작업후 수행)

3.  구문작성
sql = "insert into student(name, kor, eng, math) values(%s, %s, %s, %s)" 
#값을 직접 써도 상관은 없으나 %s를 사용하여 대입하면 정확성및 보완 효과 있음
cursor.execute(sql,("홍길동", 90,85,95)) #.execute() 명령어를 실제로 수행하는 구문
conn.commit()

sql = "select * from student"
cursor.execute(sql) #select 구문에서는 실행후 꼭 전체 내용을 가지고 오는 구문을 작성해야 함.
rows = cursor.fetchall() #조회 전부를 가지고 옴. 
    for row in rows:
        print(row)

select 구문을 execute()를 하고 함께 사용하는 함수.
.fetchall() : 전체 내용을 가지고 옴.
.fetchone() : 1개 가져 옴.

ex)
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

sql = "update student set kor=%s where name=%s"
cursor.execute(sql, (100, "홍길동"))
conn.commit()

sql = "delete from student where name=%s"
cursor.execute(sql, ("홍길동",))
conn.commit()

"""


