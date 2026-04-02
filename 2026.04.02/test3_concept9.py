import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

score = pd.read_csv("scores.csv")

score["총점"] = score[["국어", "영어", "수학"]].sum(axis=1)
score["평균"] = score[["국어", "영어", "수학"]].mean(axis=1).round(2)

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
    
score["학점"] = score["평균"].apply(grade)

print(score)

plt.bar(score["이름"], score["평균"])
plt.title("학생 평균 막대그래프")
plt.xlabel("이름")
plt.ylabel("평균")
plt.show()