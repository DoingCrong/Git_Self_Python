import pandas as pd

df = pd.read_csv("아파트.csv")

print(df)

df2=df.drop(df.columns[[0,1]], axis=1)

print(df2)

# list = df.values.tolist()

# print(type(df))
# print(list)
# print(type(list))