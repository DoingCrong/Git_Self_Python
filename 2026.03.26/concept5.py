"""
---------------------------------------------------------------------------------------------------------------
===================================================== < 상속 > ================================================
---------------------------------------------------------------------------------------------------------------

1. 상속
새로운 클래스를 만들 때 기존에 있던 클래스의 기능을 물려 받을 수 있음.
상위클래스(부모클래스=기본클래스) : super class
하위클래스(자식클래스=파생클래스) : sub class
상속을 사용하면 기존 클래스의 변경없이 기능을 추가하거나 기존 기능을 수정 가능 함.

상속 선언
자식클래스를 선언 할 때 소괄호로 부모 클래스를 포함
그러면 자식 클래스에서는 부모 클래스의 속성, 메서드는 따로 기재하지 않아도 자동으로 포함

메서드 오버라이딩
부모클래스의 메서드를 자식 클래스에서 재정의 하는 것

일반적인 메서드 오버라이딩
자식클래스에서 생성된 객체의 메서드를 부르면 부모클래스의 메서드는 무시

class 부모:
    def 함수(self):
        실행내용

class 자식(부모):
    def 함수(self):   #  같은 이름
        새로운 실행내용

부모 메소드 호출
    super()키워드 사용하여 자식 클래스 내에서 클래스 호출 가능 함.

ex)
#super class
class Account: #부모 클래스
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        print(f"{money}원 입금 -> 잔액: {self.balance}") ---> 500원 입금 -> 잔액: 1500

        
class SavingAccount(Account): #자식 클래스 소괄호안에() 부모클래스명 기재
    def __init__(self, owner, balance): #이렇게 하면 전달만 담당함.
        super().__init__(owner, balance) #부모 생성자를 호출하여 실제 데이터가 저장
    
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print(f"이자 {interest}원 추가 -> 잔액: {self.balance}") ---> 이자 75.0원 추가 -> 잔액: 1575.0

acc = SavingAccount("홍길동", 1000)

acc.deposit(500)       # 부모 메서드 사용
acc.add_interest()     # 자식 메서드 사용

#오버 라이딩
class Account: #부모클래스
    def withdraw(self, money): #부모클래스에서 만든 메서드
        print(f"{money}원 출금") #super로 부모인자를 호출하지 않았기 때문에 작동X

class SafeAccount(Account): #자식클래스
    def withdraw(self, money):
        print("보안 계좌 출금 진행") ---> 보안 계좌 출금 진행
        print(f"{money}원 출금 완료") ---> 1000원 출금 완료

        #부모 메서드를 호출하려면
        #super().withdraw(money)

acc = SafeAccount() #기본 생성자에 값을 대입하는게 아님. _init_()미사용
acc.withdraw(1000) #메서드 호출하면서 값을 전달

2. 파일 입출력
파일열기 : open
파일쓰기 : write
파일닫기 : close
파일읽기 : read

중요 : 파일을 open()으로 열기를 하면 반드시 close()해야함.
    with open()으로 열기를 하면 모든 일을 수행하고 자동으로  close()해줌

(1) 파일열기
변수 = open(파일경로, 파일열기 모드)
파일열기 모드 종류
w : 쓰기 모드(파일에 내용을 쓸 때 사용), a : 추가 모드(파일 마지막에 새로운 내용을 추가할 때 사용)
r : 일기 모드(파일을 읽기 전용), x(파일이 없을 때 새로 생성)
예)
test = open("python.txt","w")
위 파일에 경로지정이 없으면 파이썬 파일 위치와 동일 폴더에 python.txt 파일이 존재 해야함.

(2) 파일쓰기
파일객체.write("문자열")

(3) 파일닫기
파일객체.close()

ex)
#파일 쓰기 연습
filetest = open("text.txt",'w',encoding="utf-8")
#filetest = open("text.txt",'x',encoding="utf-8")
filetest.write("안녕하세요. python 파일연습 입니다.\n")
filetest.write("지금은 파일에 자료를 저장하는 연습")
filetest.close()
print("*"*80)
#파일 읽기 연습1 - 전체를 읽어서 모든 내용을 메모리에 저장. 문자열 하나로 인씩
filetest = open("text.txt","r",encoding="utf-8")
data = filetest.read() #파일에 들어있는 모든 자료를 한번에 읽어 옴.
print(data)
filetest.close()
print("*"*40)
#파일 읽기 연습2 - 한줄씩 읽어 들임. 여러 줄로 인식
filetest = open("text.txt","r",encoding="utf-8")
while True:
    data = filetest.readline() #파일에 들어있는 자료를 한줄씩 읽어 옴.
    
    if not data:
        break
    
    print(data) #한줄 공백을 지우고자 하면. print(data.strip())
    
filetest.close()
print("*"*40)
#파일 일기 연습3 - 여러줄 읽기
with open("text.txt","r",encoding="utf-8") as data:
    for line in data:
        print(line.strip())

data.close()
print("*"*40)

testfile = open("text1.txt", "a", encoding="UTF-8")
key1 = input("문장을 입력하세요!")
testfile.write(key1)
testfile.close()

testfile = open("text1.txt", "r", encoding="UTF-8")
testfile.read()
print(testfile)
testfile.close()

"""

