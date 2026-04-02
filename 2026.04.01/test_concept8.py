import pandas as pd

test = pd.read_csv("titanic.csv")
student = pd.read_csv("student_scores.csv")
student_na = pd.read_csv("student_scores_na.csv")

# print(test.columns)
# print(test["Ticket"]) #하나key에 있는 value값 뽑으려면 대괄호 하나
# print(test[["PassengerId", "Survived", "Embarked", "Sex"]]) #여러key에 있는 value값 뽑으려면 대괄호 두개



# print(student)
# score_90 = student[(student["국어"] >= 90) & (student["영어"] >= 90) & (student["수학"] >= 90) & (student["과학"] >= 90)]
# print(score_90)

# score_80 = student[(student["국어"] >= 80) & (student["영어"] >= 80) & (student["수학"] >= 80) & (student["과학"] >= 80)]
# print(score_80)

# score_50 = student[(student["국어"] < 50) | (student["영어"] < 50) | (student["수학"] < 50) | (student["과학"] < 50)]
# print(score_50)

import numpy as np

# kor_90 = student["국어"].isin(np.arange(70,101))

# all_70100 = student[
#     (student["국어"].isin(np.arange(70,101))) &
#     (student["영어"].isin(np.arange(70,101))) &
#     (student["수학"].isin(np.arange(70,101))) &
#     (student["과학"].isin(np.arange(70,101)))
# ]
# print(all_70100)

# all_70_100 = student[
#     (student["국어"].between(70, 100)) &
#     (student["영어"].between(70, 100)) &
#     (student["수학"].between(70, 100)) &
#     (student["과학"].between(70, 100))
# ]

# print(all_70100)

# print(student_na["국어"].isna())
# print(student_na["영어"].isna())
# print(student_na["수학"].isna())
# print(student_na["과학"].isna())

#print(student_na[["국어", "영어", "수학", "과학"]].isna())

# new_score = student.loc[student["국어"]>=90, ["국어", "영어", "수학", "과학"]]
# print(new_score.head(10))

# new_score.iloc[[2,3,4,5,6,7,8,9],1] = 50
# newnew_score = new_score
# print(new_score.head(10))

# print(student)

# ban_sum = student.groupby("반")[["국어","영어","수학","과학"]].sum()
# print(ban_sum)

# ban_mean = student.groupby("반")[["국어","영어","수학","과학"]].mean()
# print(ban_mean)

# ban_count = student.groupby("반")[["국어","영어","수학","과학"]].value_counts()
# print(ban_count)

# 결측치 데이터에서 행을 삭제하세요
# 합계, 평균, 학점 열을 추가하시오

print(student_na)

#print(test.dropna(axis=0).head(3))
student_clean = student.dropna(axis=0)
print(student_clean)

student_clean["총합"] = student_clean[["국어","영어","수학","과학"]].sum(axis=1)
print(student_clean)

student_clean["평균"] = student_clean[["국어","영어","수학","과학"]].mean(axis=1)
print(student_clean)

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
    
student_clean["학점"] = student_clean["평균"].apply(grade)
print(student_clean)