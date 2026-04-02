#1. 숫자를 입력받아서 함수의 인수로 전달하여 짝수인지 홀수 인지 판별하는 프로그램 작성
#(매개변수...?)

# def check(holzzak):
#     if holzzak % 2 == 0:
#         print("짝수")
#     else:
#         print("홀수")

# holzzak = check(int(input("숫자를 입력 : ")))

# #2. 숫자 2개를 입력받아서 인수로 전달하여 큰 값과 작은 값 출력

# def check2(a,b):
#     if a>b:
#         print("큰 값 : ", a)
#         print("작은 값 : ", b)
#     else:
#         print("큰 값 : ", b)
#         print("작은 값 : ", a)

# check2(int(input("숫자a : ")), int(input("숫자b : ")))

#3. 이름, 국어, 영어, 수학을 입력받아서, 총점,평균,학점을 계산하는 프로그램 작성
#단, 총점,평균,학점계산은 함수를 이용하여 수행

# school = []

# def total(kor, eng, mat):
#     return kor + eng + mat

# def average(tot):
#     return tot/3.0

# def grade(avg):
#     if avg >= 90:
#         return "A"
#     elif avg >= 80:
#         return "B"
#     elif avg >= 70:
#         return "C"
#     elif avg >= 60:
#         return "D"
#     else:
#         return "F"

# name = input("이름 : ")
# kor = int(input("국어 : "))
# eng = int(input("영어 : "))
# mat = int(input("수학 : "))

# tot = total(kor, eng, mat)
# avg = average(tot)
# grd = grade(avg)

# school.append([name, kor, eng, mat, tot, avg, grd])

# print(school)

#4. 사용자로 부터 알파벳(문자열)을 입력받아 인수로 전달하여 모든 알파벳을 대문자로 변환하는 프로그램

# def abc(text):
#    return text.upper()

# word = input("대소문자 : ")

# result = abc(word)
# print("대문자 : ", result)

#5. 단을 입력하면 해당 단의 구구단 출력 단을 인수로 전달

# def gugudan(dan):
#     for i in range(1,10):
#         print(f"{dan}*{i}={dan*i}")


# dan = int(input("단을 입력 : "))
# gugudan(dan)


"""
6. 성적프로그램 작성
3번 문제를 이용하여 무한 반복 처리
이름, 국어, 영어, 수학 점수를 입력받아
총점, 평균, 학점을 계산하고 여러 학생의 정보를 저장하는 프로그램을 작성하세요.

기능

1. 성적 입력
2. 전체 조회
3. 학생 검색
4. 학생 삭제
5. 종료

조건

학생 정보는 리스트에 저장
한 학생 정보는 딕셔너리로 저장
총점, 평균, 학점 계산은 함수로 처리
"""

#총점
def calc_total(kor, eng, math):
    return kor + eng + math

#평균
def calc_avg(total):
    return total / 3

#학점
def calc_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

#학생성적 입력
def input_student():
    name = input("이름 입력 : ")
    kor = int(input("국어 점수 입력 : "))
    eng = int(input("영어 점수 입력 : "))
    math = int(input("수학 점수 입력 : "))

#함수 호출 및 딕셔너리에 담기
    total = calc_total(kor, eng, math)
    avg = calc_avg(total)
    grade = calc_grade(avg)

    student = {
        "이름": name,
        "국어": kor,
        "영어": eng,
        "수학": math,
        "총점": total,
        "평균": avg,
        "학점": grade
    }

    return student

#타이틀 출력
def print_one_student(student):
    print(
        student["이름"], "\t",
        student["국어"], "\t",
        student["영어"], "\t",
        student["수학"], "\t",
        student["총점"], "\t",
        format(student["평균"], ".2f"), "\t",
        student["학점"]
    )

#학생 성적 출력
def print_all_students(student_list):
    if len(student_list) == 0:
        print("입력된 학생이 없습니다.")
        return

    print("이름\t국어\t영어\t수학\t총점\t평균\t학점")
    for student in student_list:
        print_one_student(student)

#학생 조회
def search_student(student_list):
    name = input("검색할 이름 입력 : ")
    found = False

    for student in student_list:
        if student["이름"] == name:
            print("이름\t국어\t영어\t수학\t총점\t평균\t학점")
            print_one_student(student)
            found = True
            break

    if not found:
        print("해당 학생이 없습니다.")

#학생 삭제
def delete_student(student_list):
    name = input("삭제할 이름 입력 : ")
    found = False

    for student in student_list:
        if student["이름"] == name:
            student_list.remove(student)
            print(name, "학생 정보 삭제 완료")
            found = True
            break

    if not found:
        print("해당 학생이 없습니다.")

#메뉴 선택
def menu():
    print()
    print("===== 성적 프로그램 =====")
    print("1. 성적 입력")
    print("2. 전체 조회")
    print("3. 학생 검색")
    print("4. 학생 삭제")
    print("5. 종료")

#리스트 선언
student_list = []

#무한 반복
while True:
    menu()
    choice = input("메뉴 선택 : ")

    if choice == "1":
        student = input_student()
        student_list.append(student)
        print("성적 입력 완료")

    elif choice == "2":
        print_all_students(student_list)

    elif choice == "3":
        search_student(student_list)

    elif choice == "4":
        delete_student(student_list)

    elif choice == "5":
        print("프로그램 종료")
        break

    else:
        print("잘못 입력했습니다.")
