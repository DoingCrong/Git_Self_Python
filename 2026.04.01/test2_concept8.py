import pandas as pd
import numpy as np

pr = pd.read_csv("product.csv")

pr = pr.dropna(axis=0)
print(pr)

pr['판매가'] = pr['공급가'] - (pr['공급가'] * pr['할인율'])
print(pr)

def check(count):
    if(count) <= 100:
        return "재고보충"
    elif(count) <= 200 and (count) > 100:
        return "재고적정"
    elif(count) <= 300 and (count) > 200:
        return "재고소비"
    
pr["비고란"] = pr["재고수량"].apply(check)
print(pr)

pr.to_csv("가공.csv", index=False, encoding="utf-8-sig")
