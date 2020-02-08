import datetime
from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    apple=request.form['apple']
    strawberry=request.form['strawberry']
    raspberry=request.form['raspberry']
    first_name=request.form['first_name']
    last_name=request.form['last_name']
    student_id=request.form['student_id']
    total_num=int(apple) + int(strawberry) +int(raspberry)
    print(f"Charging {first_name} {last_name} for {total_num} fruits")
    right_now=datetime.datetime.now()

    return render_template("checkout.html",
    apple=apple,
    strawberry=strawberry,
    raspberry=raspberry, 
    first_name=first_name,
    last_name=last_name,
    student_id=student_id,
    right_now=right_now,
    total_num=total_num)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    