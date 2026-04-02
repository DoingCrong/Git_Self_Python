"""
학생의 이름, 국어, 영어, 수학 점수를 입력받아 리스트에 저장하고, 메뉴를 통해 다음 기능을 수행하세요.

기능

학생 성적 입력
전체 조회
이름으로 검색
합격자 조회 (평균 60 이상)
종료



요구사항 
리스트 + 딕셔너리 + 함수 + while + match + class를 이용한 학생 성적 처리 프로그램
조건

학생 1명의 정보는 딕셔너리
전체 학생은 리스트
총점, 평균, 학점은 함수
메뉴는 while
그리고 class도 사용
"""
# =========================================================
# 학생 성적 처리 프로그램 (__init__ 사용 버전)
# =========================================================
# ---------------------------------------------------------
# 학생 클래스
# - 생성자에서 모든 계산 처리
# ---------------------------------------------------------
class Student:
    # [만약에 보는순서(input기준) 3. init으로 input_student에서 받았던 값 저장?]
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

        # [만약에 보는순서(input기준) 4. init으로 total, avg, grade?]
        # 생성자에서 총점, 평균, 학점까지 계산
        self.total = self.calc_total()
        self.avg = self.calc_avg()
        self.grade = self.calc_grade()

    # [만약에 보는순서(input기준) 5. 총점계산]
    # 총점 계산
    def calc_total(self):
        return self.kor + self.eng + self.math

    # [만약에 보는순서(input기준) 5-2. 평균계산]
    # 평균 계산
    def calc_avg(self):
        return self.total / 3

    # [만약에 보는순서(input기준) 5-3. 학점계산]
    # 학점 계산
    def calc_grade(self):
        if self.avg >= 90:
            return "A"
        elif self.avg >= 80:
            return "B"
        elif self.avg >= 70:
            return "C"
        elif self.avg >= 60:
            return "D"
        else:
            return "F"

    # [만약에 보는순서(input기준) 6. 다른 함수로 딕셔너리로 개인 정보 저장(return)]
    # 딕셔너리 변환 ( 중요)
    def to_dict(self):
        return {
            "name": self.name,
            "kor": self.kor,
            "eng": self.eng,
            "math": self.math,
            "total": self.total,
            "avg": self.avg,
            "grade": self.grade
        }


# ---------------------------------------------------------
# 전체 학생 리스트
# ---------------------------------------------------------

# [만약에 보는순서(input기준) 7. 리스트 생성(이건 언제해도 상관없?)]
students = []


# ---------------------------------------------------------
# 학생 입력 
# ---------------------------------------------------------
def input_student():
    print("\n[학생 성적 입력]")
    # [만약에 보는순서(input기준) 2. input_student함수?객체?(class내부아님)에서 필요한 값 입력]
    name = input("이름: ")
    kor = int(input("국어: "))
    eng = int(input("영어: "))
    math = int(input("수학: "))

    # [만약에 보는순서(input기준) 2-2. 객체 생성(class호출)]
    # 객체 생성 (여기서 __init__ 자동 실행) 호출
    s = Student(name, kor, eng, math)

    # [만약에 보는순서(input기준) 8. input_student함수에서 calss에서 딕셔너리로 저장된걸 리스트로 저장]
    # 딕셔너리로 변환 후 리스트 저장
    students.append(s.to_dict())

    print("저장 완료")


# ---------------------------------------------------------
# 전체 조회
# ---------------------------------------------------------
def show_all():
    print("\n[전체 조회]")

    if not students:
        print("데이터 없음")
        return

    print("이름\t국어\t영어\t수학\t총점\t평균\t학점")

    for s in students:
        print(f"{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t"
              f"{s['total']}\t{s['avg']:.2f}\t{s['grade']}")


# ---------------------------------------------------------
# 이름 검색
# ---------------------------------------------------------
def search_name():
    name = input("검색 이름: ")
    found = False

    for s in students:
        if s["name"] == name:
            print(f"{s['name']} {s['avg']:.2f} {s['grade']}")
            found = True

    if not found:
        print("없음")


# ---------------------------------------------------------
# 합격자 조회
# ---------------------------------------------------------
def pass_students():
    print("\n[합격자]")

    found = False

    for s in students:
        if s["avg"] >= 60:
            print(f"{s['name']} {s['avg']:.2f} {s['grade']}")
            found = True

    if not found:
        print("합격자 없음")


# ---------------------------------------------------------
# 메뉴 [만약에 보는순서(input기준) 1. input으로 1번을 받음(class로 받는 매개변수는 개인정보로 기준)]
# ---------------------------------------------------------
while True:
    print("\n1. 입력 2. 전체 3. 검색 4. 합격 5. 종료")
    menu = input("선택: ")

    match menu:
        case "1":
            input_student()
        case "2":
            show_all()
        case "3":
            search_name()
        case "4":
            pass_students()
        case "5":
            print("종료")
            break
        case _:
            print("잘못된 입력")