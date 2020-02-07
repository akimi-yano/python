# 1. http://localhost:5000 - should display 8 by 8 checkerboard
# 2. http://localhost:5000/4 - should display 8 by 4 checkerboard
# 3. http://localhost:5000/(x)/(y) - should display x by y checkerboard.  
# For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  
# Before you pass x or y to Jinja, 
# please remember to convert it to integer first (so that you can use x or y in a for loop)

from flask import Flask,  render_template
app = Flask(__name__)

@app.route("/")
def eight_by_eight():
    return render_template("index.html", num_height = 8, num_width = 8)

@app.route("/4")
def eight_by_four():
    return render_template("index.html", num_height = 8, num_width = 4)

@app.route("/<number1>/<number2>")
def x_by_y(number1, number2):
    return render_template("index.html", num_height = int(number1), num_width = int(number2))

if __name__ == "__main__":
    app.run(debug=True)