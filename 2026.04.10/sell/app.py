from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

#home
@app.route("/")
def home():
    return redirect(url_for("box"))

@app.route("/box", methods=['POST'])
def box():
    product = request.form["product"].lower().strip()
    count = int(request.form['count'].strip())
    cost = int(request.form['cost'].strip())

    if product == "q":
        return "프로그램을 종료합니다."
    
    price = count*cost
    sale=0
    sales_price=0

    if price>=3000000:
        sale=0.03
        sales_price = price-price*sale
    elif price>=2000000:
        sale=0.015
        sales_price = price-price*sale
    else:
        sales_price = price

    sale=sale*100

    return render_template("result.html",
                           product, count, cost, price, sale, sales_price)

if __name__=="__main__":
    app.run(debug=True)