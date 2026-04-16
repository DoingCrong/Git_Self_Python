"""
텍스트 마이닝 기반 예측
텍스트 데이터를 컴퓨터가 이해할 수 있도록 가공하고 분석하여 예측 하도록 함.
분석 예측 : 주가상승/하락 예측, 인기 키워드 예측
1. 데이터 수집 : 뉴스 API(크롤링)
2. 전처리(불필요한 문자 제거), 형태소 분석, 불용어 제거
3. 특징 추출(단어 빈도, 키워드 추출)
4.
"""

from collections import Counter
import re
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

text = """
삼성전자 실적개선
주가 상승 기대
주가 상승
호재 뉴스
상승 기대감
"""
#무식한 방법?으로 때려맞추기
positive_words =['상승','기대','호재','실적개선','회복','성장'] #긍정적인
negative_words = ['하락','악재','적자','감소','위기','손실']    #부정적인

#1. 글자를 단어로 분리(리스트에 저장)
words = re.findall(r'\w+',text)

#2. 단어 개수 세기(리스트에 들어있는 단어를 숫자화)(딕셔너리형태로)
counter = Counter(words)

#3. 출력
print("추출된 단어 : ", words)
print("단어 빈도수 : ", counter)

#번외 : 딕셔너리로 담겨있는 counter의 value값
print(counter['주가']) #딕셔너리 형태인지 체크하려고 돌려봄

#4. plt(차트)출력
x = list(counter.keys()) #counter에 있는 딕셔너리중 key만을 따로 x변수에 수록
y = list(counter.values()) #counter에 있는 딕셔너리중 value만을 따로 y변수에 수록

plt.figure() #도화지 생성?
plt.bar(x,y) #bar 타입으로 생성 / line..
plt.title("단어 빈도수 막대그래프") #차트제목
plt.xlabel("단어") #X축 제목
plt.ylabel("빈도수") #Y축 제목

plt.show() #plt출력