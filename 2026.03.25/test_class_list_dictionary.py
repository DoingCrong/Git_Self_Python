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
#class
class Test:
    #초기값
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

        계산구문
        self.total = self.total()
        self.average = self.average()
        self.grade = self.grade()
        self.passed = self.passed()

    def total(self):
        return self.kor+self.eng+self.mat
        
    def average(self):
        return self.total / 3.0
        
    def grade(self):
        if self.average >= 90:
            return "A"
        elif self.average >= 80:
            return "B"
        elif self.average >= 70:
            return "C"
        elif self.average >= 60:
            return "D"
        else:
            return "F"

    def passed(self):
        if self.grade != "F":
            return "합격"
        else:
            return "불합격"

    def dic(self):
        return {
            "이름" : self.name,
            "국어" : self.kor,
            "영어" : self.eng,
            "수학" : self.mat,
            "총점" : self.total,
            "평균" : self.average,
            "학점" : self.grade,
            "합격" : self.passed
        }
    
    #selectAll
    def selectAll(self):
        print(school)

school = []

while True:
    print("===합격자성적===")
    print("1. 학생 성적 입력")
    print("2. 전체 조회")
    print("3. 이름으로 조회")
    print("4. 합격자 조회")
    print("0. 종료\n")

    choice = int(input("입력 : "))

    if choice==0:
        break
    elif choice==1:
        name = input("이름 : ")
        kor = int(input("국어 : "))
        eng = int(input("영어 : "))
        mat = int(input("수학 : "))
        
        t = Test(name, kor, eng, mat) #class 호출

        school.append(t.dic())
        print("성적입력완료")
    elif choice==2:
        t.selectAll()

    elif choice==3:
        selectByName()

    elif choice==4:
        passcheck()

