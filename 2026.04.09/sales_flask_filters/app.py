
from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

app = Flask(__name__)
# 한글 표시용 설정
plt.rcParams["font.family"] = "Malgun Gothic"
plt.rcParams["axes.unicode_minus"] = False

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "sales.csv"
STATIC_DIR = BASE_DIR / "static"

# 데이터 읽기
def load_data():
    df = pd.read_csv(CSV_PATH)
    df["date"] = pd.to_datetime(df["date"])
    df["operating_profit"] = df["revenue"] - df["marketing_spend"]
    return df

# 검색용 목록
def get_filter_options(df):
    years = sorted(df["year"].dropna().unique().tolist())
    regions = sorted(df["region"].dropna().unique().tolist())
    products = sorted(df["product_line"].dropna().unique().tolist())
    return years, regions, products

# 검색 조건 적용
def apply_filters(df, year="", region="", product_line=""):
    result = df.copy()

    if year:
        result = result[result["year"] == int(year)]

    if region:
        result = result[result["region"] == region]

    if product_line:
        result = result[result["product_line"] == product_line]

    return result

# 연도별 매출
def get_yearly(df):
    return df.groupby("year").agg(
        total_revenue=("revenue", "sum")
    ).reset_index()

# 월별 매출
def get_monthly(df):
    return df.groupby("month").agg(
        total_revenue=("revenue", "sum")
    ).reset_index().sort_values("month")

# 지역별 매출
def get_region(df):
    return df.groupby("region").agg(
        total_revenue=("revenue", "sum")
    ).reset_index()

# 제품별 수익성
def get_product(df):
    return df.groupby("product_line").agg(
        total_revenue=("revenue", "sum"),
        operating_profit=("operating_profit", "sum")
    ).reset_index()

# 차트 저장
def save_bar_chart(x, y, filename, title):
    plt.figure(figsize=(9, 5))
    plt.bar(x, y)
    plt.title(title)
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(STATIC_DIR / filename)
    plt.close()

def save_line_chart(x, y, filename, title):
    plt.figure(figsize=(9, 5))
    plt.plot(x, y, marker="o")
    plt.title(title)
    plt.grid(True)
    plt.xticks(rotation=20)
    plt.tight_layout()
    plt.savefig(STATIC_DIR / filename)
    plt.close()

# 공통 검색 옵션
def common_context():
    df = load_data()
    years, regions, products = get_filter_options(df)
    return {
        "years": years,
        "regions": regions,
        "products": products,
    }

@app.route("/")
def home():
    return render_template("index.html", **common_context())

@app.route("/yearly")
def yearly():
    df = load_data()
    year = request.args.get("year", "")
    region = request.args.get("region", "")
    product_line = request.args.get("product_line", "")

    filtered = apply_filters(df, year, region, product_line)
    result = get_yearly(filtered)
    save_line_chart(result["year"], result["total_revenue"], "year.png", "연도별 매출")

    return render_template(
        "result.html",
        title="연도별 매출",
        description="검색 조건을 적용한 연도별 매출 합계입니다.",
        tables=result.to_dict("records"),
        columns=result.columns.tolist(),
        chart="year.png",
        current_menu="yearly",
        selected_year=year,
        selected_region=region,
        selected_product=product_line,
        **common_context()
    )

@app.route("/monthly")
def monthly():
    df = load_data()
    year = request.args.get("year", "")
    region = request.args.get("region", "")
    product_line = request.args.get("product_line", "")

    filtered = apply_filters(df, year, region, product_line)
    result = get_monthly(filtered)
    save_line_chart(result["month"], result["total_revenue"], "month.png", "월별 매출")

    return render_template(
        "result.html",
        title="월별 매출",
        description="검색 조건을 적용한 월별 매출 합계입니다.",
        tables=result.to_dict("records"),
        columns=result.columns.tolist(),
        chart="month.png",
        current_menu="monthly",
        selected_year=year,
        selected_region=region,
        selected_product=product_line,
        **common_context()
    )

@app.route("/region")
def region():
    df = load_data()
    year = request.args.get("year", "")
    region_value = request.args.get("region", "")
    product_line = request.args.get("product_line", "")

    filtered = apply_filters(df, year, region_value, product_line)
    result = get_region(filtered)
    save_bar_chart(result["region"], result["total_revenue"], "region.png", "지역별 매출")

    return render_template(
        "result.html",
        title="지역별 매출",
        description="검색 조건을 적용한 지역별 매출 합계입니다.",
        tables=result.to_dict("records"),
        columns=result.columns.tolist(),
        chart="region.png",
        current_menu="region",
        selected_year=year,
        selected_region=region_value,
        selected_product=product_line,
        **common_context()
    )

@app.route("/product")
def product():
    df = load_data()
    year = request.args.get("year", "")
    region = request.args.get("region", "")
    product_line = request.args.get("product_line", "")

    filtered = apply_filters(df, year, region, product_line)
    result = get_product(filtered)
    save_bar_chart(result["product_line"], result["operating_profit"], "product.png", "제품별 영업이익")

    return render_template(
        "result.html",
        title="제품별 수익성",
        description="검색 조건을 적용한 제품별 매출과 영업이익입니다.",
        tables=result.to_dict("records"),
        columns=result.columns.tolist(),
        chart="product.png",
        current_menu="product",
        selected_year=year,
        selected_region=region,
        selected_product=product_line,
        **common_context()
    )

if __name__ == "__main__":
    app.run(debug=True)
