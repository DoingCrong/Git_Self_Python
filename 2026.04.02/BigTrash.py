import pandas as pd


df = pd.read_csv("경기도_화성시_대형폐기물처리수수료정보_20260220.csv", encoding='utf-8') 

result1 = df.groupby("대형폐기물명")["수수료"].agg(['sum', 'mean'])
#result1.columns = ["대형폐기물명", "수수료_합계", "수수료_평균"]


result2 = df.groupby(["대형폐기물명", "대형폐기물구분명"])["수수료"].agg(['sum', 'mean'])
#result2.columns = ["대형폐기물명", "대형폐기물구분명", "수수료_합계", "수수료_평균"]


print("대형폐기물명별 : 수수료 합계/평균")
print(result1.head())
print("대형폐기물명별/구분명별 : 수수료 합계/평균")
print(result2.head())


# result1.to_csv("화성시_폐기물_통계1.csv", index=False, encoding='utf-8-sig')
# result2.to_csv("화성시_폐기물_통계2.csv", index=False, encoding='utf-8-sig')