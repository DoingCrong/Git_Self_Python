"""
사용자로 부터 숫자 2개를 입력받아서 사칙연산을 수행 후
그 결과 값을 출력하세요

입력화면
처음숫자 : 
두번째 숫자 : 

두수의 합 :
두수의 차 :
두수의 곱 : 
두수의 제? :
"""

# num1 = float(input("숫자 1 : "))
# num2 = float(input("숫자 2 : "))
# op = input("기호(+,-,*,/) : ")

# if op=="+":
#     print("계산결과 : ",num1+num2)
# elif op=="-":
#     print("계산결과 : ",num1-num2)
# elif op=="*":
#     print("계산결과 : ",num1*num2)
# elif op=="/":
#     print("계산결과 : ",num1/num2)
# else:
#     print("잘못된 기호입니다.")

#구구구단
# dan = int(input("단을 입력하세요 : "))

# print("="*20)
# print(f"출력 : {dan}단")
# print("="*20)
# for i in range(9):
#     print(f"{dan}*{i+1} = {dan*(i+1)}")

"""
사용자로 부터 이름, 국어, 영어, 수학을 입력받아서 총점, 평균, 학점을 계산하여
리스트에 수록하여 출력하는 프로그램을 작성하세요

입력화면

이름 : 홍길동
국어 : 100
영어 : 100
수학 : 100

출력화면
=========================================
                                      성적표
=========================================
이름     국어     영어     수학      총점      평균      학점
홍길동   100      100      100       300       100        A
"""

# name = input("이름 : ")
# kor = int(input("국어 : "))
# eng = int(input("영어 : "))
# mat = int(input("수학 : "))

# total = kor+eng+mat
# average = total/3.0

# if average>=90:
#     grade="A"
# elif average>=80:
#     grade="B"
# elif average>=70:
#     grade="C"
# elif average>=60:
#     grade="D"
# else:
#     grade="F"

# info = [name, kor, eng, mat, total, average, grade]

# head = "=" * 30
# head2 = head+"\n\t    성적표\n"+head
# print(head2)

# print(" 이름\t  국어 영어 수학 총점 평균\t\t학점")
# print(info)

# students = []
# while True:
#     # 입력
#     name = input("이름 입력 : ")
#     if name=="Q" or name=="q": #name.lower()=="q":
#         break
#     kor = int(input("국어 점수 : "))
#     eng = int(input("영어 점수 : "))
#     math = int(input("수학 점수 : "))

#     # 계산
#     total = kor + eng + math
#     avg = total / 3

#     # 학점 계산
#     if avg >= 90:
#         grade = 'A'
#     elif avg >= 80:
#         grade = 'B'
#     elif avg >= 70:
#         grade = 'C'
#     elif avg >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'

#     # 리스트에 저장
#     students.append([name, kor, eng, math, total, avg, grade])

# #출력
# print("="*60)
# print("\t\t\t성적표")
# print("="*60)
# print("이름\t국어\t영어\t수학\t총점\t평균\t학점")
# print("="*60)
# for s in students:
#     print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]:.2f}\t{s[6]}")

"""
-----------------------------------------------------------------------------
위 프로그램을 딕셔너리로 작성하세요.
1. 한사람 자료입력 후 종료
-------------------------------------------------------------------------------

2. 무한 반복 
이름이 Q 또는 q를 입력하면 입력 종료 하고 나서 출력을 한다.
리스트, 딕셔너리를 이용한 여러사람 입력 받기
"""


# students = {
#     "name" : input("이름 입력 : "),
#     "kor" : int(input("국어 : ")),
#     "eng" : int(input("영어 : ")),
#     "math" : int(input("수학 : "))
# }

# total = students.get("kor") + students.get("eng") + students.get("math") 
# avg = total / 3.0

# if avg >= 90:
#     grade = 'A'
# elif avg >= 80:
#     grade = 'B'
# elif avg >= 70:
#     grade = 'C'
# elif avg >= 60:
#     grade = 'D'
# else:
#     grade = 'F'

# students["total"] = total
# students["avg"] = avg
# students["grade"] = grade
# # 출력

# print("="*60)
# print("\t\t\t성적표")
# print("="*60)
# print("이름\t국어\t영어\t수학\t총점\t평균\t학점")
# print("="*60)

# print(students.items())

# student = {}

# # 입력
# student['name'] = input("이름 입력 : ")
# student['kor'] = int(input("국어 점수 : "))
# student['eng'] = int(input("영어 점수 : "))
# student['math'] = int(input("수학 점수 : "))

# # 계산
# student['total'] = student['kor'] + student['eng'] + student['math']
# student['avg'] = student['total'] / 3

# # 학점 계산
# if student['avg'] >= 90:
#     student['grade'] = 'A'
# elif student['avg'] >= 80:
#     student['grade'] = 'B'
# elif student['avg'] >= 70:
#     student['grade'] = 'C'
# elif student['avg'] >= 60:
#     student['grade'] = 'D'
# else:
#     student['grade'] = 'F'

# # 출력
# print("\t\t\t성적표")
# print("="*60)
# print("이름\t국어\t영어\t수학\t총점\t평균\t학점")
# print("="*60)
# print(f"{student['name']}\t, {student['kor']}\t, {student['eng']}\t, {student['math']}\t, "
#       f"{student['total']}\t, {student['avg']:.2f}\t, {student['grade']}")

students = []

while True:
    name = input("이름(q 입력시 종료) : ")
    if name.lower() == 'q':
        break

    student = {}
    student['name'] = name
    student['kor'] = int(input("국어 : "))
    student['eng'] = int(input("영어 : "))
    student['math'] = int(input("수학 : "))

    # 계산
    student['total'] = student['kor'] + student['eng'] + student['math']
    student['avg'] = student['total'] / 3

    # 학점
    if student['avg'] >= 90:
        student['grade'] = 'A'
    elif student['avg'] >= 80:
        student['grade'] = 'B'
    elif student['avg'] >= 70:
        student['grade'] = 'C'
    elif student['avg'] >= 60:
        student['grade'] = 'D'
    else:
        student['grade'] = 'F'

    students.append(student)

# 출력
print("\t\t\t성적표")
print("="*60)
print("이름\t국어\t영어\t수학\t총점\t평균\t학점")
print("="*60)

for s in students:
    print(f"{student['name']}\t {student['kor']}\t{student['eng']}\t{student['math']}\t, "
      f"{student['total']}\t {student['avg']:.2f}\t{student['grade']}")
