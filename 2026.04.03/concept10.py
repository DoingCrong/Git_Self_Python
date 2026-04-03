"""
범례지정(Legend) : 그래프에 데이터의 종류를 표시하기 위한 텍스트
legend() : 그래프에 범례 표시
xlim() : x축이 표시되는 범위 지정[xmin, xmax]
ylim() : y축이 표시되는 범위 지정[ymin, ymax]
axis() : x,y축이 표시되는 범위 지정[xmin, xmax, ymin, ymax]
입력 값이 없으면 자동으로 지정

plot() 함수의 marker="s", "D"
plot() 함수의 color = "색상"
대표색상
'b' : blue, 'g' : green, 'r' : red, 'y' : yellow, 'k' : black, 'w' : white

xticks(), yticks() : 각각 x축, y축 눈금 설정

scatter() : 산점도 시각

ex)
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [3, 6, 9, 12], marker="s") #네모 모양
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.xlim([0, 5])      
plt.ylim([0, 15])    

plt.show()

plt.plot([1,2,3,4],[1,5,9,15],marker="D") #다이야 모양
plt.axis([0,6,0,20]) #x축시작 0~6, y축시작 0~20
plt.show()

plt.plot([1, 2, 3, 4], [2.0, 3.0, 5.0, 10.0], 'r') #빨강색
plt.plot([1, 2, 3, 4], [2.0, 2.8, 4.3, 6.5], color = 'violet') #보라색
plt.plot([1, 2, 3, 4], [2.0, 2.5, 3.3, 4.5], color = 'green') #초록색

plt.xlabel('X-Label')
plt.ylabel('Y-Label')

plt.show()

x = [1, 2, 3]
years = ['2022', '2023', '2024']
values = [300, 100, 700]

plt.bar(x, values, color=['r', 'g', 'b'], width=0.4)
#plt.bar(x, values, color=['r', 'g', 'b'], width=0.8)

plt.xticks(x, years) #x축 눈금을 년도에 표시

plt.show()

---------------------------------------------------------------------------------------------------------------
===================================================== < BeautifulSoup  > ================================================
---------------------------------------------------------------------------------------------------------------

◎ HTML/XML문서를 분석해서 원하는 데이터를 쉽게 추출할 수 있도록 하는 라이브러리
1) 웹페이지 정보 가져오기
    파이썬  Requests라이브러리 사용
2) HTML 소스를 분석하여 원하는 정보 얻기
    파이썬 BeautifulSoup 라이브러리 사용
    
◎ 웹 크롤링 개념
    사용자 브라우저 접속 -> 해당 주소의 서버에게 요청(request)
    -> 웹 서버 구성에 필요한 정보 코드 전달(response)
    -> 브라우저는 서버가 전달 해준 정보를 해석하여 사용자 화면에 표시


◎ 설치
pip install beautifulsoup4
pip install requests

◎ 라이브러리 불러오기
from bs4 import BeautifulSoup

1. 웹페이지 분석하기
변수(soup) = BeautifulSoup(웹문서,"html.parser")
html을 파이썬에서 읽을 수 있게 파싱(파이썬 객체로 변환)
html이라는 변수에 저장한 html소스를 .parser를 붙여 변환
.parser 파이썬 내장 메서드임

ex)
from bs4 import BeautifulSoup
html = "<html><body><h1>안녕하세요. 크롤링 연습입니다.</h1></body></html>" #html 구문
test = BeautifulSoup(html,"html.parser") # html구문을 변수에 담기
print(test.h1.text) # 출력


BeautifulSoup 데이터를 텍스트로 반환
soup : soup의 데이터를 모두 가져와서 텍스트로 반환
soup.contents : soup의 데이터를 모두 가져와서 리스트로 반환
soup.stripped_strings : 공백도 함께 제거하여 텍스트로 반환

ex)
# html = #""
# <html>
#    <body>
#    <h1 id = 'title'>라이브러리 활용</h1>
#    <p id = 'body'>웹 데이터 수집</p>
#    <p class = 'scraping'>2026-04-03</p>
#    <p class = 'scraping'>데이터 웹 크로링 기초 연습</p>
#    </body>
# </html>
# #""

soup = BeautifulSoup(html, "html.parser")
for text in soup:
    print(text)

print("*"*50)
for text1 in soup.contents:
    print(text1)

print("*"*50)   
for text2 in soup.stripped_strings:
    print(text2)

    
Find 함수
변수 = soup.find(class_="scraping")
변수.string

find()
    id, class, element등을 검색 함
find : 조건에 해당하는 첫 번째 정보만 검색
    - 클래스 이름을 알 경우, class_형태로 사용
find_all : 조건에 해당하는 모든 정보 검색
string : 태그 내부의 텍스트만 출력

select()
    css 선택
    soup.select("div.class명")

.text 추출
    tag.text

ex)
soup = BeautifulSoup(html, "html.parser")
text1 = soup.find(id="title") #html구문에서 id가 "title"을 찾아서 변수에 담아라
print(text1)
print("-"*50)

text2 = soup.find(class_='scraping') #첫번째 정보만 찾아서 변수에 담아라
print(text2)
print("-"*50)

text3 = soup.find_all(class_='scraping') # scraping이라는 모든 정보를 찾아서 변수에 담아라
print(text3)
print("-"*50)

text4 = soup.find_all(id="title") # title이라는 모든 정보를 찾아서 변수에 담아라
print(text4)
print("-"*50)
"""
from bs4 import BeautifulSoup

html =  """
<html>
   <body>
   <h1 id = 'title'>라이브러리 활용</h1>
   <h2 id = 'title'>라이브러리 활용2</h2>
   <p id = 'body'>웹 데이터 수집</p>
   <p class = 'scraping'>2026-04-03</p>
   <p class = 'scraping'>데이터 웹 크로링 기초 연습</p>
   </body>
<html>
"""
soup = BeautifulSoup(html, "html.parser")

text3 = soup.find_all(class_='scraping') # scraping이라는 모든 정보를 찾아서 변수에 담아라
print(text3)
print("-"*50)

text4 = soup.find_all(id="title") # title이라는 모든 정보를 찾아서 변수에 담아라
print(text4)
print("-"*50)