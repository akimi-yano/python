from flask import Flask,render_template
app = Flask(__name__)

@app.route("/play")
def show_three_boxes():
    return render_template("playground.html", num = 3)

@app.route("/play/<number>")
def show_x_boxes(number):
    return render_template("playground.html", num = int(number))

@app.route("/play/<number>/<color>")
def show_x_color_boxes(number, color):
    return render_template("playground.html", num = int(number), col= color)



if __name__ == "__main__":
    app.run(debug=True)

