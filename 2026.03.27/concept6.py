"""
파이썬 파일 모드(추가)

w : 쓰기(덮어쓰기 )-파일이 없으면 생성
w+ : 읽기 + 쓰기(덮어쓰기)-파일이 없으면 생성
r : 읽기(파일이 없으면 오류발생)
r+ : 읽기+쓰기(파일이 없으면 오류발생)
a : 추가(쓰기만)-파일이 없으면 생성
a+ : 읽기 + 추가 (파일이 없으면 생성)

--------------------------------------
a
file = open("test.txt", "a")  --> 추가로 파일을 열어서
file.write("내용")  # 가능
file.read()         #  오류

예)
students = [] 
with open("score.txt", "r", encoding="utf-8") as file: #만약에 score.txt파일이 미 존재를 하면 오류발생
for line in file: 
   data = line.strip().split(",") 
   students.append(data)
------------------------------------------
a+
file = open("test.txt", "a+") ---> 파일을 읽기와 추가를 동시에 수행하여 읽어들이면 커서가 마지막에 위치 함
file.write("내용")  # 가능
file.seek(0)        # 읽기를 하려면 커서를 처음 위치 이동 필요함.(a+와 함께 필수 사용)
print(file.read())  # 가능

예)
students = [] 
file = open("score.txt", "a+", encoding="utf-8") #파일이 미존재를 하면 파일을 생성
file.seek(0) # 파일 포인터를 맨 앞으로 이동 필수
for line in file: 
   data = line.strip().split(",") 
   students.append(data) 

file.close() 

예외처리 : 프로그램 실행 중 발생할 수 있는 오류(예외)를 미리 대비하여 프로그램의 비정상 종료부분을 처리
구문)
try:
    오류가 발생할 수 있는 구문
except:
    오류 발생 시 실행 구문
    

try:  오류 발생 가능 코드
except: 오류 처리
else:  정상 실행 시
finally: 무조건 실행

#예외처리 기본 구문
try:
    num = int(input("숫자 입력 : "))
    result = 10 / num
    print("결과 :", result)

except:
    print("오류 발생! 숫자를 제대로 입력하세요.")
    
#예외처리 발생 오류 저장
try:
    num = int(input("숫자 입력 : "))
    result = 10 / num

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")

except ValueError: #파이썬 기본 예외처리 타입 - 값(value)이 잘못되었다라고 인식.
    print("숫자만 입력하세요.")

#예외처리 오류 발생, 오류 미 발생, 무조건 수행
try:
    num = int(input("숫자 입력 : "))
    result = 10 / num

except Exception as e:
    print("오류 :", e)

else:
    print("정상 실행 결과 :", result)

finally:
    print("프로그램 종료")
    
    
#반복 예외 처리
while True:
    try:
        num = int(input("숫자 입력 : "))
        print("입력 성공 :", num)
        break

    except ValueError:
        print("숫자만 입력하세요!")
        
#예외 처리 발생시 오류 메시지 출력
try:
    a = int(input("숫자 : "))
    b = int(input("숫자 : "))
    print(a / b)

except Exception as e:
    print("에러 내용 :", e)

넘파이 : 수치계산 라이브러리
선형대수 연산에 필요한 다차원 배열과 배열 연산을 수행하는 다양한 함수를 포함
배열(Array) 을 기반으로 연산을 수행하며, 머신러닝·데이터분석에서 필수적으로 사용

넘파이를 하려면 패키지를 먼저 설치를 해야함 : pip install numpy (콘솔박스에 입력)
설치후 사용하려면 : import numpy as np (평균적으로 이름을 축약해서 사용함. np로)

넘파이에서 사용하는 배열 : 넘파이에서는 배열은 ndarray 또는 array 칭함

넘파이 배열과 파이썬 배열은 다른 성격을 가짐

numpy array : [10,20,30]+[10,20,30] = [20,40,60]
python array : [10,20,30]+[10,20,30] = [10,20,30,10,20,30]

numpy array : [10,20,30]+5 = [15,25,30]
python list : [10,20,30]*2 = [10,20,30,10,20,30]

NumPy 배열
numpy는 모든 배열의 값이 기본적으로 같은 타입
numpy에서는 각 차원을 축을 axis 라고 함.

1차원 배열
shape(4,) -> 1 2 3 4
             axis 0

2차원 배열
shape(2,4)
      axis 0   1.0 2.0 3.0 4.0
      (열)     2.1 3.2 4.4 5.5
             axis 1(행)

3차원 배열
shape(2,4,2) -> 면,행,열

NumPy 배열 대표 속성 값
배열.shape : 배열의 각 축(axis)의 크기
배열.ndim : 축의 개수
배열.dtype : 각 요소의 타임
배열.itemsiz : 각 요소의 타입의 bytes 크기
배열.size : 전체 요소의 개수

배열 생성 방법 : 
np.array([1,2,3,4])
np.arange(12).reshape(3,4) -> 배열의 전체 크기를 12개로 선언하면서 배열의 구조를 다시 정의하여 3행 4열로 정의
np.zeros((2,3)) -> 모든 값을 0으로 채우는 2행 3열 배열 생성
np.ones((2,3)) -> 모든 값을 1로 채우는 2행 3열 배열 생성
np.empty((2,3)) -> 초기 값이 없는 2행 3열 배열 생성

넘파이 데이터 생성하기

np.arange() : 시작~끝미만을 일정 간격으로 배열 생성
사용방법) np.arange(시작, 끝, 증가값)
np.linspace() : 시작~끝을 포함하여 사이를 균등하게 나눔
사용방법) 
np.linsace(시작, 끝, 생성갯수)
.reshape() : 배열의 차원을 변경할때 사용하는 함수
배열.reshape(행, 열), np.reshape(배열, (행, 열))

ex)
import numpy as np
n = int(input("개수 입력 : "))

arr = []

for i in range(n):
    num = int(input(f"{i+1}번째 값 입력 : "))
    arr.append(num)

print("결과 :", arr)

score = np.array(arr)
print(score)

"""