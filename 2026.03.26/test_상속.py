# 부모 클래스
class Student:
    # 생성자
    def __init__(self, name, kor, eng, math):
        self.name = name      # 이름
        self.kor = kor        # 국어 점수
        self.eng = eng        # 영어 점수
        self.math = math      # 수학 점수

    # 총점 계산 메서드
    def total(self):
        return self.kor + self.eng + self.math

    # 평균 계산 메서드
    def average(self):
        return self.total() / 3

    # 기본 출력 메서드
    def display(self):
        print("이름 :", self.name)
        print("국어 :", self.kor)
        print("영어 :", self.eng)
        print("수학 :", self.math)
        print("총점 :", self.total())
        print("평균 :", round(self.average(), 2))


# 자식 클래스
class GradeStudent(Student):
    # 부모 클래스를 상속받아서 학점 기능만 추가
    def grade(self):
        avg = self.average()

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


# 객체 생성
s1 = GradeStudent("홍길동", 90, 85, 100)

# 부모에게서 상속받은 display() 사용
s1.display()

# 자식 클래스의 grade() 사용
print("학점 :", s1.grade())