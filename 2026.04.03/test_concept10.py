import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_scores.csv")

df["합계"] = df[["국어", "영어", "수학", "과학"]].sum(axis=1)

print(df["합계"])

ban = df.groupby("반")["합계"]

print(ban)

# print(ban)

plt.plot(ban, df["합계"], marker="s") #네모 모양
plt.xlabel('반')
plt.ylabel('합계')

plt.show()