"""
---------------------------------------------------------------------------------------------------------------
===================================================== < 데이터 시각화 라이브러리 > ================================================
---------------------------------------------------------------------------------------------------------------
1. 데이터 시각화 라이브러리
Matplotlib

① 설치 방법 : pip install matplotlib
② 사용법 : import matplotlib.pyplot as plt

◎ 기본 사용법
x=[1,2,3,4]
y=[10,20,25,30]
plt.plot(x,y) : plt.plot() #꺽은선 그래프 그리기
plt.bar(x,y) : 막대 그래프
plt.pie() : 파이 그래프
plt.hist() : 히스토그램

◎ 그래프 관련 명령어
plt.title() : 제목
plt.xlabel() : x축 제목
plt.ylabel() : y축 제목
plt.grid() : 격자 그리기

◎ plt.show()
plt.show() : 그래프를 화면에 

1) 한개의 숫자 리스트 입력
① 한 개의 숫자 리스트 형태로 입력하면 y값으로 인식
② x값은 기본적으로 [0,1,2,3,...]으로 설정
③ 파이썬 튜븛, 넘파이 배열 형태도 사용 가능 함.
④ plt.show() 함수로 화면에 그래프를 나타냄 (print()불필요함)

2) 두 개의 숫자 리스트 입력
① 두 개의 숫자 리스트 형태로 값을 입력하면 순서대로 x,y 값으로 인식
② 순서쌍(x,y)으로 매칭된 값이 좌표평면 위에 시각화

ex)
#선그래프
#하나의 값을 입력(X축)
import matplotlib.pyplot as plt
plt.plot([2,3,4,5])
plt.show()

#두개의 값을 입력(X축, Y축)
plt.plot([1,2,3,4],[1,4,9,15])
plt.show()

#막대그래프
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = "Malgun Gothic" #한글깨짐방지용
plt.rcParams['axes.unicode_minus'] = False    #한글깨짐방지용

names = ["홍길동", "김철수", "이영희"]
scores = [85,90,78]

plt.bar(names, scores) #x축에 names, y축에 scores
plt.title("학생성적") #차트제목
plt.xlabel("이름")    #x축제목
plt.ylabel("점수")    #y축제목

plt.show()
"""
import matplotlib.pyplot as plt

