import datetime
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/checkout", methods=['POST'])
def checkout():
    total_num = int(request.form['strawberry_num']) + int(request.form['rasberry_num']) + int(request.form['apple_num'])
    right_now = datetime.datetime.now()
    return render_template("checkout.html", name =request.form['name'], student_id = request.form['student_id'], strawberry_num = request.form['strawberry_num'], rasberry_num = request.form['rasberry_num'], apple_num = request.form['apple_num'], total_num = total_num, now=right_now.strftime("%B %d,%Y %I:%M:%S%p"))


if __name__ == "__main__":
    app.run(debug=True)