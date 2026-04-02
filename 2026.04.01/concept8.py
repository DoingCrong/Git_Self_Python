"""
---------------------------------------------------------------------------------------------------------------
===================================================== < Pandas > ================================================
---------------------------------------------------------------------------------------------------------------
1. pandas
① 데이터 처리 라이브러리 : pandas
② 파이썬에서 사용하는 데어터 분석 라이브러리
③ 행과 열로 이루어진 2차원 데이터를 효율적으로 가공(표형태)
④ 판다스 : 시리즈(Series)와 데이터프레임(DataFrame) 두가지 지원
⑤ 시리즈 : 1차원 배열(열)
⑥ 시리즈는 데이터가 순차적으로 나열(인덱스와 value가 일대일 대응)
⑦ 인덱스 : 위치, value :  값


◎ 데이터프레임 : 2차원(행,열)
설치 : pip install pandas
사용법 : import pandas as pd

◎ 판다스 버전 업그레이드 설치
pip install --upgrade pip
pip install pandas --upgrade

ex)
import pandas as pd
#1차원 배열
data = pd.Series([10, 20, 30, 40])
print(data) ---> 0    10
                 1    20
                 2    30
                 3    40
                 dtype: int64

#2차원 배열
data = {
    "이름": ["홍길동", "이순신", "유관순"],
    "국어": [90, 80, 70],
    "영어": [85, 75, 65]
}

df = pd.DataFrame(data)
print(df) --->     이름  국어  영어
                0  홍길동  90  85
                1  이순신  80  75
                2  유관순  70  65

◎ 판다스 파일 불러오기
판다스는 다양한 형태의 외부 파일을 읽어와서 데이터프레임으로 변환하는 함수를 제공
File Format             read                   writer
CSV                     read_csv               to_csv
Excel                   read_excel             to_excel
JSON                    read_json              to_json
SQL                     read_sql               to_sql
HTML                    read_html              to_html

#kaggle
https://www.kaggle.com/competitions

ex)
import pandas as pd

test = pd.read_csv("titanic.csv")


◎ 판다스 내용확인하기
.head()      # 상위 5개
.tail()      # 하위 5개
.info()      # 구조 확인(행과 열의 크기, 컬럼명, 컴럼명 결측치, 컬럼명 데이터 타입 등)
.shape       # (행, 열)크기
.columns     # 컬럼명
.type()       # 데이터 타입 확


ex)
import pandas as pd

test = pd.read_csv("titanic.csv")
print(test.head()) #상위 5개(기본)추출
print(test.head(10)) #상위 10개 추출

print(test.columns) #컬럼명만 추출

print(test.tail()) #하위 5개(기본)추출
print(test.tail(10)) #하위 10개 추출

print(test.shape) ---> (891, 12) #전체 891행이고 12열(컬럼명)

print(test.info()) # 구조 확인(행과 열의 크기, 컬럼명, 컴럼명 결측치, 컬럼명 데이터 타입 등)

print(type(test)) ---> <class 'pandas.DataFrame'>


◎ 판다스 특정 열 선택
열  1개 선택 = 시리즈 객체 반환


◎ 데이터프레임의 열 데이터를 1개만 선택할 때는 2가지 방식
① 대괄호([])안에 열 이름을 큰따옴표("")와 함께 입력
print(df["이름"])
② 도트(.)다음에 열 이름을 입력
t = df.이름

ex)
import pandas as pd

data = {
    "이름": ["홍길동", "이순신", "유관순"],
    "국어": [90, 80, 70],
    "영어": [85, 75, 65],
    "수학": [100, 90, 80]
}

df = pd.DataFrame(data)
print(df)
print("="*30)

print(df["이름"]) #value 출력

t = df.이름
print("="*30)
print(t)


◎ 데이터프레임의 여러 데이터 방식
① 여러 개 선택 = 데이터프레임 객체 반환
② 데이터프레임의 열 데이터를 여러개 선택할 때는 
2중 대괄호([[]])안에 열 이름을 큰따옴표("")와 함께 입력
print(df[["이름","국어","영어","수학"]])

1개의 열을 데이터프레임 객체로 추출하려면 [[]]로 사용.

ex)
import pandas as pd

data = {
    "이름": ["홍길동", "이순신", "유관순"],
    "국어": [90, 80, 70],
    "영어": [85, 75, 65],
    "수학": [100, 90, 80]
}
df = pd.DataFrame(data)

print(df[["이름","국어","영어","수학"]])
print("="*30)

◎ 판다스 데이터 필터링
① 불리언 인덱싱 : True 값을 가진 행만을 추출한다.
② .isin() : 각각의 요소가 데이터프레임 또는 시리즈에 존재하는지 파악하여 True/False 값 반환
③ 불리언인덱싱 + .isin() : 데이터의 특정 범위만 추출
④ .insna() : 결측 값은 True 반환, 긔 외에는 False 반환
⑤ .notna() : 결측 값이 False 반환, 나머지는 True 반환

ex1)
import pandas as pd

data = {
    "이름": ["홍길동", "이순신", "유관순"],
    "국어": [90, 80, 70],
    "영어": [85, 75, 65],
    "수학": [100, 90, 80]
}
df = pd.DataFrame(data)
print(df)
print(df[(df["국어"] >= 80) & (df["영어"] >= 70)]) #& 조건이 모두 참일때 True
print("="*30)
print(df[(df["국어"] >= 80) | (df["영어"] >= 70)]) #| 조건이 모두 거짓일 때 False

ex2)
import pandas as pd

test = pd.read_csv("titanic.csv")
student = pd.read_csv("student_scores.csv")

print(test["Pclass"])
print(test["Pclass"].isin([1])) #Pclass 1이면 True, 아니면 False

ex3)
import pandas as pd

test = pd.read_csv("titanic.csv")

import numpy as np

age2040 = test[test["Age"].isin(np.arange(20,40))]
print(age2040) #numpy를 이용하여 20~39까지의 조건의 값을 추출

ex4)
print(test["Age"].head(10))

print(test["Age"].isna()) # True라고 나오면 결측치 데이터가 존재

print(test["Age"].isna()[0:7]) # 0부터 7미만까지 결측치 데이터 확인
                                (True라고 나오면 결측치 데이터가 존재)

ex5)
print(test["Age"].notna()[0:7]) # False라고 나오면 결측치 데이터가 존재
                                (즉, True값은 결측치 데이터가 아님)

2. 결측치 데이터 제거
① .dropna(axis=0) == .dropna() #결측치 값이 있는 행을 삭제
                              (즉, 고객정보1(가로) 전체정보 삭제)
② .dropna(axis=1)             #결측치 값이 있는 열 전체 삭제
                              (즉, 데이터명(세로) 정보 삭제)

ex)
print(test.head(3))

print(test.dropna(axis=0).head(3)) # 결측치가 존재하는 고객정보(가로) 전체정보 전체 삭제

print(test.dropna(axis=1)) # 결측치가 존재하는 데이터명(세로) 열 전체 삭제

3. 이름과 인덱스로 특정 행과 열을 선택
① .loc[] : 행이름과 열이름을 사용하여 선택
dataframe객체.loc[행이름 또는 열이름]
② .iloc[] : 행번호와 열번호를 사용
dataframe객체.iloc[행번호 또는 열번호]

ex)
name350=test.loc[test["Age"]>35,["Name","Age"]]
print(name350.head())

name350.iloc[[1,2,3],0]="No name" # 1,2,3번째 행(에서) ~ 0번째열 값(을) No name 으로 변경
name = name350
print(name)

4. 판다스 데이터 통계함수
.mean() : 평균
.sum() : 합산
.median() : 중앙값
.describe() : 다양한 통계량 요약
.agg() : 여러 개의 열에 다양한 함수를 적용
         모든 열에 여러 함수를 대입(적용) : group객체.agg([함수1, 함수2, ...])
         각 열마다 다른 함수를 대입(적용) : group객체.agg({'열1':함수1,'열2':함수2,...})
.groupby() : 그룹별 집계함수
.value_counts() : 값의 개수
.max() : 최대값
.min() : 최소값
.std() : 표준편차

print(round(test["Age"].mean(),2)) ---> 29.7

print(test["Age"].sum()) ---> 21205.17

print(test["Age"].median()) ---> 28.0

print(test["Age"].describe()) #전체

print(test.agg({"Age":["min","max","median","std"],
                "Fare":["min","max","mean","median"]}))

#성별과 클래스를 이용하여 그룹을하여 나이와 요금의 평균계산
print(test.groupby(["Sex","Pclass"])[["Age","Fare"]].mean())

#성별을 기준으로 그룹하여 생존율의 평균계산
survive = test.groupby("Sex")["Survived"].mean()
print(survive)

result = test.groupby("반").agg({
    "국어": ["mean", "sum", "std"],
    "영어": ["mean", "sum", "std"],
    "수학": ["mean", "sum", "std"],
    "과학": ["mean", "sum", "std"]
})

print(result)
result2 = test.groupby("반")["반"].value_counts()
print(result2)

#클래스별로 개수 계산
print(test["Pclass"].value_counts())

5. 판다스 행과 열 추가와 삭제
행추가
    DataFrame.loc['새로운 행 이름'] = 데이터 값
열추가
    DataFrame객체['추가열이름'] = 데이터 값
행삭제
    DataFrame.drop(index, axis=0)
열삭제
    DataFrame.drop(변수명, axis=1)

print(t.shape)
newRow = t.iloc[0,:] #t변수에 있는 iloc[0,:] 0번째 행의 자료(열)을 새로운 변수에 담기.
t.loc[981]=newRow
print(t)
print(t.shape)

import numpy as np
t = t.drop(np.arange(880,890), axis = 0)
print(t)

t = t.drop('Pclass',axis=1)
print(t)

새로운 컬럼 추가
데이터프레임명["새로운컬럼명"] = 데이터

tt = pd.read_csv("tt.csv")
print(tt)    

ex)

# [열 추가] Numpy where를 사용하여 '합격여부'를 한 번에 결정
# 평균이 60점 이상이면 'Pass', 아니면 'Fail'
test["합격여부"] = np.where(test["평균"] >= 60, "Pass", "Fail")

# [열 삭제] '학점' 열이 더 이상 필요 없다고 가정하고 삭제
test = test.drop("학점", axis=1)

# [행 삭제] 첫 번째 행(index 0) 삭제
test = test.drop(0, axis=0)

print(test.head())
# [열 추가] Numpy를 사용하여 과목들의 '평균'을 계산하여 추가
# .values를 쓰면 Numpy array로 변환되어 연산이 빨라집니다.
subjects = ["국어", "영어", "수학", "과학"]
student["평균"] = np.mean(student[subjects].values, axis=1)

# [행 추가] loc를 사용하여 새로운 학생 데이터 추가
# 변수명과 컬럼 순서에 맞게 값을 배치
student.loc["new_student"] = [85, 90, 70, 80, 81.25] 

1)
student["학점"] ="F"
student.loc[student["평균"]>=60,"학점"] = "D"
student.loc[student["평균"]>=70,"학점"] = "C"
student.loc[student["평균"]>=80,"학점"] = "B"
student.loc[student["평균"]>=90,"학점"] = "A"
print(student)

2)
def grade(avg):
    if(avg) >= 90:
        return "A"
    elif(avg) >= 80:
        return "B"
    elif(avg) >= 70:
        return "C"
    elif(avg) >= 60:
        return "D"
    else:
        return "F"
    
student["학점"] = student["평균"].apply(grade)

print(student)

함수를 호출하여 구문 수행
apply(호출하고자하는 함수 이름)
구간 정해주기
cut()

ex)
student["학점"] =pd.cut(
    student["평균"],
    bins = [0,60,70,80,90,100],
    labels=["F","D","c","B","A"],
    right=False #구간 포함 방향 설정(왼쪽 포함, 오른쪽 제외)
)

---------------------------------------------------------------------------------------------------------------
===================================================== < 직접DataFrame만들기 > ================================================
---------------------------------------------------------------------------------------------------------------
import pandas as pd

# 빈 리스트 생성
data = []

# 1명 입력
name = input("이름 입력 : ")
kor = int(input("국어 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))

# 리스트에 저장
data.append([name, kor, eng, math])

# 판다스 데이터프레임 생성
df = pd.DataFrame(data, columns=["이름", "국어", "영어", "수학"])

print(df)

"""

import pandas as pd
import numpy as np

test = pd.read_csv("titanic.csv")
student = pd.read_csv("student_scores.csv")
student_na = pd.read_csv("student_scores_na.csv")






