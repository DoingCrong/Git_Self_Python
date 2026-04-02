school=[]

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

name = input("이름 : ")
kor = int(input("국어 : "))
eng = int(input("영어 : "))
mat = int(input("수학 : "))

t = Test(name, kor, eng, mat) #클래스 호출

school.append([t.name, t.kor, t.eng, t.mat, t.total(), t.average(), t.grade()])

print(school)

