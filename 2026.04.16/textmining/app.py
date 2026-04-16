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
LG전자 악재
삼성물산 위기
"""
#무식한 방법?으로 때려맞추기
positive_words =['상승','기대','호재','실적개선','회복','성장'] #긍정적인
negative_words = ['하락','악재','적자','감소','위기','손실']    #부정적인

#1. 글자를 단어로 분리(리스트에 저장)
words = re.findall(r'\w+',text)

score=0

for word in words:
    if word in positive_words:
        score+=1
        print(word, " : 긍정(+1)")
    elif word in negative_words:
        score-=1
        print(word, " : 부정(-1)")
    else:
        print(word, " : 중립(0)")

print("="*40)
print("최종점수 : ", score)

if score>0:
    print("예측 결과 : 상승")
elif score<0:
    print("예측 결과 : 하락")
else:
    print("예측 결과 : 중립")