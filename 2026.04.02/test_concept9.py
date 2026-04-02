import pandas as pd

df = pd.read_json("student_scores.json")

#총점 평균 학점 추가
df["총점"] = df[["국어", "영어", "수학"]].sum(axis=1)
df["평균"] = df[["국어", "영어", "수학"]].mean(axis=1).round(2)

df["학점"] = "F"
df.loc[df["평균"] >= 60, "학점"] = "D"
df.loc[df["평균"] >= 70, "학점"] = "C"
df.loc[df["평균"] >= 80, "학점"] = "B"
df.loc[df["평균"] >= 90, "학점"] = "A"

# JSON에 저장
df.to_json("result.json", orient="records", force_ascii=False, indent=4)
#orient="records" : 한 행을 하나의 딕셔너리로 저장
#force_ascii=False : 한글깨짐 방지
#indent=4 : 들여쓰기 해줌 (4칸씩)

print("JSON 저장 완료")