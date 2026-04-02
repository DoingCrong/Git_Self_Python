# 부모 클래스
class Student:
    # 생성자
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    # 총점 계산
    def total(self):
        return self.kor + self.eng + self.math

    # 평균 계산
    def average(self):
        return self.total() / 3

    # 기본 출력 메서드
    def display(self):
        print("이름 :", self.name)
        print("총점 :", self.total())
        print("평균 :", round(self.average(), 2))


# 자식 클래스
class GradeStudent(Student):
    # 학점 계산 메서드
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

    # 부모의 display() 메서드를 재정의(오버라이딩)
    def display(self):
        print("===== 성적표 =====")
        print("이름 :", self.name)
        print("국어 :", self.kor)
        print("영어 :", self.eng)
        print("수학 :", self.math)
        print("총점 :", self.total())
        print("평균 :", round(self.average(), 2))
        print("학점 :", self.grade())
        print("==================")


# 객체 생성
s1 = GradeStudent("김철수", 88, 79, 91)

# 오버라이딩된 display() 호출
s1.display()