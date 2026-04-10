from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 입력된 판매 자료를 저장할 리스트
sales_list = []

# 허용 상품명
products = ["키보드", "마우스", "스캐너", "모니터", "본체"]


@app.route("/")
def home():
    return redirect(url_for("sale_input")) #url_for : 함수 이름 직접 호출


@app.route("/input", methods=["GET", "POST"])
def sale_input():
    message = ""

    if request.method == "POST":
        product = request.form["product"].strip()

        # q 입력 시 차트 페이지로 이동
        if product.lower() == "q":
            return redirect(url_for("chart_view"))

        # 상품명 체크
        if product not in products:
            message = "상품명은 키보드, 마우스, 스캐너, 모니터, 본체 중 하나만 입력하세요."
            return render_template("input.html", message=message, sales_list=sales_list)

        try:
            qty = int(request.form["qty"])
            price = int(request.form["price"])

            if qty <= 0 or price <= 0:
                message = "수량과 단가는 1 이상 입력하세요."
                return render_template("input.html", message=message, sales_list=sales_list)

            # 판매금액
            sale_amount = qty * price

            # 할인 계산
            if sale_amount >= 3000000:
                discount = sale_amount * 0.03
            elif sale_amount >= 2000000:
                discount = sale_amount * 0.015
            else:
                discount = 0

            # 실판매액
            real_amount = sale_amount - discount

            sales_list.append({
                "product": product,
                "qty": qty,
                "price": price,
                "sale_amount": sale_amount,
                "discount": int(discount),
                "real_amount": int(real_amount)
            })

            message = "자료가 저장되었습니다. 계속 입력하세요. 종료하려면 상품명에 q 입력."

        except ValueError:
            message = "수량과 단가는 숫자로 입력하세요."

    return render_template("input.html", message=message, sales_list=sales_list)


@app.route("/chart")
def chart_view():
    # 상품별 판매금액 합계와 건수
    product_sum = {p: 0 for p in products}
    product_count = {p: 0 for p in products}

    for row in sales_list:
        product = row["product"]
        # '판매금액의 평균' 기준
        product_sum[product] += row["sale_amount"]
        product_count[product] += 1

    # 상품별 평균 판매금액 계산
    labels = []
    avg_values = []

    for p in products:
        labels.append(p)
        if product_count[p] > 0:
            avg_values.append(round(product_sum[p] / product_count[p], 2))
        else:
            avg_values.append(0)

    return render_template(
        "chart.html",
        labels=labels,
        avg_values=avg_values,
        sales_list=sales_list
    )


if __name__ == "__main__":
    app.run(debug=True)