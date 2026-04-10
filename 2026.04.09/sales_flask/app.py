# app.py
from flask import Flask, render_template
import pandas as pd
import numpy as np
import matplotlib

# Flask 서버에서 차트를 파일로 저장하기 위해 Agg 사용
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

app = Flask(__name__)
# 한글 표시용 설정
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

# 현재 파일이 있는 폴더 기준 경로
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "sales.csv"
STATIC_DIR = BASE_DIR / "static"

# 1. 데이터 읽기
def load_data():

    df = pd.read_csv(CSV_PATH)

   
    df["date"] = pd.to_datetime(df["date"]) #csv파일중에 date 컬럼을 날짜 형식으로 변경(계산때문)
     #이익률 계산
    df["operating_profit"] = df["revenue"] - df["marketing_spend"] #영업이익 계산
   
    return df

# ------------------------------------------------------------
# 2. 연도별 매출 분석
# ------------------------------------------------------------
def get_yearly_sales(df):
    """
    연도별 총매출, 평균매출 계산
    """
    result = df.groupby("year").agg(  #년도별로 그룹을 수행하고 여러 함수를 한번에 수향
        total_revenue=("revenue", "sum"), #매출액 합계
        avg_revenue=("revenue", "mean"), #매출액 평균
        total_units=("units_sold", "sum") #판매수량 합계
    ).reset_index() #그룹결과를 일반 데이터프레임 형태로 변경해줌
    

 
    result["total_revenue"] = result["total_revenue"].round(2)
    result["avg_revenue"] = result["avg_revenue"].round(2)
    print(result)
    return result


# 3. 지역별 매출 분석
def get_region_sales(df):
    """
    지역별 총매출, 평균매출 계산
    """
    
    result = df.groupby("region").agg( #지역으로 그룹수행후 여러 함수 수행
        total_revenue=("revenue", "sum"),
        avg_revenue=("revenue", "mean"),
        total_units=("units_sold", "sum")
    ).reset_index()

    result["total_revenue"] = result["total_revenue"].round(2)
    result["avg_revenue"] = result["avg_revenue"].round(2)

    # 총매출 기준 내림차순 정렬
    result = result.sort_values("total_revenue", ascending=False)

    return result

# ------------------------------------------------------------
# 4. 제품별 수익성 분석
# ------------------------------------------------------------
def get_product_profitability(df):
    """
    제품별 매출, 마케팅비, 영업이익, 이익률 계산
    """
    result = df.groupby("product_line").agg(
        total_revenue=("revenue", "sum"),
        marketing_spend=("marketing_spend", "sum"),
        operating_profit=("operating_profit", "sum"),
 
    ).reset_index()

    result["total_revenue"] = result["total_revenue"].round(2)
    result["marketing_spend"] = result["marketing_spend"].round(2)
    result["operating_profit"] = result["operating_profit"].round(2)
    

    # 이익 기준 내림차순 정렬
    result = result.sort_values("operating_profit", ascending=False)

    return result


# 5. 바차트 그리기(연도별, 지역별)
def save_bar_chart(x, y, title, xlabel, ylabel, filename):

    plt.figure(figsize=(10, 5)) #페이지 크기 지정 가로 10인치, 세로 5인치
    plt.bar(x, y) #차트 종류 지정 막대형 차트
    plt.title(title) #차트 제목 지정
    plt.xlabel(xlabel) #x축 제목
    plt.ylabel(ylabel) #y축 제목
    plt.xticks(rotation=20) #x축 레이블 회전 각도
    plt.tight_layout() #차트 영역안에 여백 자동 조정
    plt.savefig(STATIC_DIR / filename) #파일을 지정한 경로에 저장
    plt.close() #plt 종료

#꺽은선 그래프
def save_line_chart(x, y, title, xlabel, ylabel, filename):

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker="o") #선 그래프 작성/각 값을 동그라미로 표시
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(STATIC_DIR / filename)
    plt.close()


# 6. 화면 라우팅
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/yearly")
def yearly():

    #연도별 매출 분석
    df = load_data()
    result = get_yearly_sales(df)

    # 차트 저장
    save_line_chart( #차트 합수 호출 할때 각각 대입값 전송
        result["year"],
        result["total_revenue"],
        "연도별 총매출",
        "연도",
        "매출",
        "연도별매출분석차트.png" #저장할 차트 이름
    )

    return render_template(
        "result.html", #출력하기 위한 html 파일 호출
        title="연도별 매출 분석", #html에서 사용할 변수에 값 수록
        description="연도별 총매출, 평균매출, 판매수량을 확인합니다.",
        tables=result.to_dict(orient="records"),
        columns=result.columns.tolist(),
        chart_file="연도별매출분석차트.png"
    )

@app.route("/region")
def region():
    """
    지역별 매출 분석
    """
    df = load_data()
    result = get_region_sales(df)

    # 차트 저장
    save_bar_chart(
        result["region"],
        result["total_revenue"],
        "지역별 총매출",
        "지역",
        "매출",
        "지역별매출분석차트.png"
    )

    return render_template(
        "result.html",
        title="지역별 매출 분석",
        description="지역별 총매출, 평균매출, 판매수량을 확인합니다.",
        tables=result.to_dict(orient="records"),#데이터프레임을 딕셔너리로 변환
        columns=result.columns.tolist(), #딕셔너리를 다시 리스트로 변환(그래야 html에서 사용가능)
        chart_file="지역별매출분석차트.png" #그림 파일 이름
    )

@app.route("/product")
def product():
    """
    제품별 수익성 분석
    """
    df = load_data()
    result = get_product_profitability(df)

    # 차트 저장
    save_bar_chart(
        result["product_line"],
        result["operating_profit"],
        "제품별 영업이익",
        "제품",
        "영업이익",
        "제품별수익성차트.png"
    )

    return render_template(
        "result.html",
        title="제품별 수익성 분석",
        description="제품별 총매출, 마케팅비, 영업이익, 평균이익률을 확인합니다.",
        tables=result.to_dict(orient="records"),
        columns=result.columns.tolist(),
        chart_file="제품별수익성차트.png"
    )

# ------------------------------------------------------------
# 7. 프로그램 시작
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
