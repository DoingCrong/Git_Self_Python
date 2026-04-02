"""
13. 집합 자료형(set)
교집합(&)
합집합(|)
차집합(-)

add() : 한개의 값을 추가
update() : 여러개의 값을 추가
remove() : 특정 값을 제거

ex)
test1 = {1,2,3,4,5}
test2 = {1,3,5,7,9}
print(test1 | test2) ---> {1, 2, 3, 4, 5, 7, 9} #합집합 : 두집합의 모든 요소를 합친것
print(test1 & test2) ---> {1, 3, 5} #교집합 : 두집합의 공통으로 포함된 요소만 만든것
print(test1 - test2) ---> {2, 4} #차집합 : 한집합에서 다른 집합에 있는 요소를 뺀것
print(test2 - test1) ---> {9, 7}

test1.add(6) #한개만 추가가능
print(test1) ---> {1, 2, 3, 4, 5, 6}

test1.update([10,20]) #반드시 list형식으로 추가해야함
print(test1) ---> {1, 2, 3, 4, 5, 6, 20, 10} 

test1.remove(1) #특정한 값 하나를 삭제
print(test1) ---> {2, 3, 4, 5, 20, 10}

14. 부울 자료형(bool)
① 주로 참, 거짓을 나타낼때 사용
② 주로 조건문등에서 반환 값으로 사용

◎ 변하지 않는 참, 거짓
① 문자열, 리스트, 튜블, 딕셔너리 등의 값이 비어 있으면 False(거짓)
② 문자열, 리스트, 튜블, 딕셔너리 등의 값이 비어 있지 않으면 Trye(참)

if문에서 참, 거짓 판별
ex)
print("abcd" == "abcd") ---> True
print(10<5) ---> False

---------------------------------------------------------------------------------------------------------------
===================================================== < 문법 > ================================================
---------------------------------------------------------------------------------------------------------------

1. 사용자 입력(input)
◎ input()
① 괄호 안에 입력한 내용을 '프롬포트 문자열'이라고 함.
② 사용자로부터 입력을 받고자 할때 사용
③ 입력 받은 내용을 변수에 대입하여 사용
④ input()으로 입력받은 자료는 무조건 문자열 자료(★중요☆)

ex)
print(input("이름을 입력하세요 : ")) ---> 이름을 입력하세요 : 홍길동 ---> 홍길동

name = input("이름을 적어주세요 : ") 
print(type(name)) ---> 이름을 적어주세요 : gpt ---> <class 'str'>
name = input("숫자를 적어주세요 : ")
print(type(name)) ---> 숫자를 적어주세요 : 13 ---> <class 'str'>

2. 숫자로변환(int, float)
int() : (문자열을) 숫자 정수로 변환
float() : (문자열을) 숫자 실수로 변환

ex)
str1 = input("숫자1을 입력하세요 : ") ---> 13
str2 = input("숫자2를 입력하세요 : ") ---> 12
print(str1+str2) ---> 1312
                ↓↓↓↓↓↓↓↓
str1 = int(input("숫자1을 입력하세요 : "))
str2 = int(input("숫자2를 입력하세요 : "))
print(str1+str2) ---> 25

3. 문자로변환(str)
str() : 숫자등을 문자열로 변환

ex)
int1 = 123
print(type(int1)) ---> <class 'int'>
print(type(str(int1))) ---> <class 'str'>

4. 출력함수(print)
◎ print()
① 자료형을 출력하는 함수
② 큰따옴표("")로 둘러싸인 문자열은 더하기(+) 연산과 동일함.
 (즉, ""연속하여 사용할시 +기호가 포함되어있다.)

ex)
print("안녕하세요" "파이썬" "프로그래밍입니다.") ---> 안녕하세요파이썬프로그래밍입니다.
print("안녕하세요" ,"파이썬" ,"프로그래밍입니다.") ---> 안녕하세요 파이썬 프로그래밍입니다.

5. 조건문
◎ if()
① 조건이 참일 경우 실행, 조건이 거짓일 경우 패스
② 조건 옆에는 반드시 콜론(:)이 나와야 함 (★중요☆)
③ 들여쓰기 반드시 해야 함 (★중요☆)
④ if문을 다 작성 하였으면 들여쓰기 없는 다음 줄로 작성...

ex)
#조건이 참인 경우
test1 = True
if test1:
    print("파이썬의 if문 공부") ---> 파이썬의 if문 공부

◎ else()
① 조건이 거짓일때 수행 구문 작성
② if와 else는 같은 열에 있어야 함 (★중요☆)

if 조건:
    참 수행
else:
    거짓 수행

ex)
#조건이 거짓인 경우
test2 = False
if test2:
    print("파이썬 if구문")
else:
    print("파이썬 else구문") ---> 파이썬 else구문

◎ elif()
① java에서 elseif
② 조건이 세개 이상일 때 사용
③ if와 elif, else 같은 열에 있어야 함 (★중요☆)
④ 조건 옆에는 반드시 콜론(:)이 나와야 함, 들여쓰기 반드시 해야 함 (★중요☆)

if 조건1:
    조건1이 참일때
elif 조건2:
    조건2가 참일때
elif 조건3:
    조건3이 참일때
else:
    나머지 조건문 수행

ex)
test3=75
if test3>=90:
    print("수")
elif test3>=80:
    print("우")
elif test3>=70:
    print("미") ---> 미
elif test3>=60:
    print("양")
else:
    print("가")

6. in / not in 연산자
데이터 안에 찾고자 하는 것이 있는지 없는지 확인하는 연산자

ex)
if 'k' in 'python':
    print(True) 
else:
    print(False) ---> False

if 'k' not in 'python':
    print(True) ---> True
else:
    print(False)

7. pass 키워드
① 조건은 만족하지만(True) 아무 문장도 수행하고 싶지 않을 때 사용
② 프로그램 작성시 골격 만들 때 주로 사용

ex)
test = ['사과', '딸기', '바나나']
if '딸기' in test:
    pass ---> 

8. 관계 연산자
두 개의 값 비교하여 참, 거짓 판별
==, !=, >, <, >=, <=

8-2. 논리 연산자
not(논리 부정) : 한개의 값이 False면 결과 True반환, True이면 False 반환
and(논리 곱셈) : 두개의 값이 모두 True일때만 True반환, 나머지는 False 반환
or(논리 합) : 두개의 값이 모두 False일때만 False 반환, 나머지는 True 반환

ex)
print(1>2 or 1<2) ---> True
print(1>2 and 1<2) ---> False

9. 반복문
◎ for
① 특정 부분을 반복 작업을 할때 사용
② list와 튜플, 그리고 문자열의 첫 번째 요소부터 마지막 요소까지 차례로...
③ 변수에 대입등에 사용
④ 반드시 콜론(:)이 나와야 함 (★중요☆)
⑤ 들여쓰기 반드시 해야 함 (★중요☆)

for 변수 in 리스트(또는 튜플, 문자열):
    #반복적으로 수행할 구문

ex)
test5 = "korea"
for i in test5:
    print(i) ---> k
                  o
                  r
                  e
                  a

◎ range()
① 반복문과 함께 잘사용

※java에서 비슷한 역할 = for(i=0, i<=count, i++) {...
range(5) = 0~4까지 반복 수행(총 5개 범위)
range(1,5) = 1부터 5미만
range(1,10,2) = 1부터 10미만까지 2씩증가

ex)
for i in range(5): #반복문 시작값은 0부터 시작해서 5미만까지(0~4)
    print('반복문 수행',i) ---> 반복문 수행 0
                                반복문 수행 1
                                반복문 수행 2
                                반복문 수행 3
                                반복문 수행 4

◎ list() (리스트로 변환)
range(범위)를 리스트로 변경하면 범위 안에서 어떤 값이 있는지를 확인 가능 함.

ex)
print(range(5)) ---> range(0, 5)
print(list(range(5))) ---> [0, 1, 2, 3, 4]
print(list(range(1,10))) ---> [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,2))) ---> [1, 3, 5, 7, 9]

◎ 리스트 반복
ex)
test6 = ['사과', '배', '귤', '바나나', '딸기']
for i in test6:
    print(i) ---> 사과
                  배
                  귤
                  바나나
                  딸기

◎ 딕셔너리 반복                  
ex)
test7 = {
    "name" : "홍길동",
    "job" : "도둑"
}

for i in test7:
    print(i,":") ---> name :
                      job :
#변수를 찍으면 key값 출력
    
for i in test7:
    print(":",test7[i]) --> : 홍길동
                            : 도둑
#변수의첨자[]를 찍으면 value값 출력
                            
for i in test7:
    print(i,":",test7[i]) ---> name : 홍길동
                               job : 도둑
#즉, i : key / test7[i] : value

9-2. 다중 for문
※java에서 비슷한 역할 
for(i=1, i<=9, i++) {
    for(j=1, j<=9, j++){
    i*j=i*j
    }
}
ex)
for i in range(1,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}") ---> 구구단(1~9) 전체 값 출력
    print() ---> 줄바꿈용도

9-3. while
◎ while()
① 반드시 콜론(:)이 나와야 함 (★중요☆)
② 들여쓰기 반드시 해야 함 (★중요☆)

while 조건:
    수행구문1
    수행구문2

ex)
count = 0
while count < 5:
    print("count :", count)
    count = count+1
    print("끝") ---> count : 0
                     끝
                     count : 1
                     끝
                     count : 2
                     끝
                     count : 3
                     끝
                     count : 4
                     끝

◎ break
break
① 반복문을 벗어날때 사용하는 키워드

ex)
a=10
count=0

while a>3:
    count = count+1
    a=a+1
    if count>20:
        break
    print("a = ",a,"\t count = ", count) ---> a =  11          count =  1
                                              a =  12          count =  2
                                              a =  13          count =  3
                                              ....
                                              a =  30          count =  20
print("반복문 종료") ---> 반복문 종료

◎ 무한루프
while True: ...

ex)
count = 0
while True:
    if count > 10:
        break
    count=count+1
    print(count)
print("무한 루프 탈출 : ",count) ---> 1
                                      2
                                      3
                                      ...
                                      11
                                      무한 루프 탈출 :  11
"""
