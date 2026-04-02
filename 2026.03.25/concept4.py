"""
---------------------------------------------------------------------------------------------------------------
===================================================== < 함수 > ================================================
---------------------------------------------------------------------------------------------------------------

1. 클래스
① 클래스 : 동일한 무언가를 계속 만들어 낼 수 있는 설계 도면(붕어빵틀)
② 객체 : 클래스로 만들어진 것(슈크림붕어빵, 팥붕어빵등...)
③ 인스턴스 : 객체를 사용함
④ 속성(변수) : 데이터(학생이름, 국어, 영어, 수학등...)
⑤ 생성자 : _init_() 객체가 실행되면 자동으로 실행, 자동 생성은 되지 않음
⑥ 메서드(함수) : 기능 수행(총점, 평균, 학점등)

◎ 클래스 선언
calss 클래스이름:
    클래스내용

class 클래스이름:
    def 메서드 이름(self, 추가적인 매개변수):
        #메서드 이름(함수)에서 ☆첫번째 매개변수는 반드시 self★

◎ _init_()
① 이것을 사용하는 주된 이유는 초기값을 세팅하기위하여 사용한다.     

ex)
class test:
    def test1(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

class Person:
    def __init__(self, name):
        self.name = name

p=Person("홍길동")
print(p.name) ---> 홍길동

# _init_() 사용 안하면 나중에 값을 따로 넣어야 함.
class Person:
    pass

p = Person()
p.name = "홍길동" #따로 넣어야함
print(p.name) ---> 홍길동

#클래스 정의
class Person:
    # 생성자 (객체가 만들어질 때 자동 실행)
    def __init__(self, name, age):
        self.name = name  # 이름 저장
        self.age = age    # 나이 저장

    # 메서드 (기능)
    def introduce(self):
        print("이름:", self.name)
        print("나이:", self.age)

# 객체 생성
p1 = Person("홍길동", 20)
# 메서드 호출
p1.introduce() ---> 이름: 홍길동
                    나이: 20

class Test:
    #초기값 대입
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng 
        self.mat = mat

    def total(self):
        return self.kor+self.eng+self.mat
    
    def average(self):
        return self.total() / 3 #total은 객체단위로 가져와서
    
    def grade(self):
        if self.average() >= 90:
            return "A"
        elif self.average() >= 80:
            return "B"
        elif self.average() >= 70:
            return "C"
        elif self.average() >= 60:
            return "D"
        else:
            return "F"

t = Test("홍길동", 80, 90, 100) #클래스 호출

print("이름 : ", t.name)
print("국어 점수 : ",t.kor)
print("영어 점수 : ", t.eng)
print("수학 점수 : ",t.mat)
print("총점 : ", t.total()) #객체 단위로 가져옴
print("평균 :", t.average())
print("평균: {:.2f}".format(t.average())) #.format() 함수 사용 
print(f"평균: {t.average():.2f}") # 향상 f"구문 사용
print("평균:", round(t.average(), 2)) #함수 round()함수 사용
print("*"*20)
print("학점", t.grade())
"""

class Test:
    #초기값 대입
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng 
        self.mat = mat

    def total(self):
        return self.kor+self.eng+self.mat
    
    def average(self):
        return self.total() / 3 #total은 객체단위로 가져와서
    
    def grade(self):
        if self.average() >= 90:
            return "A"
        elif self.average() >= 80:
            return "B"
        elif self.average() >= 70:
            return "C"
        elif self.average() >= 60:
            return "D"
        else:
            return "F"

t = Test("홍길동", 80, 90, 100) #클래스 호출


print("이름 : ", t.name)
print("국어 점수 : ",t.kor)
print("영어 점수 : ", t.eng)
print("수학 점수 : ",t.mat)
print("총점 : ", t.total()) #객체 단위로 가져옴
print("평균 :", t.average())
print("평균: {:.2f}".format(t.average())) #.format() 함수 사용 
print(f"평균: {t.average():.2f}") # 향상 f"구문 사용
print("평균:", round(t.average(), 2)) #함수 round()함수 사용
print("*"*20)
print("학점", t.grade())

