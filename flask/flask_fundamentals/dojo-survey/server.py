from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def fill_servey():
    return render_template("index.html")

@app.route("/result", methods = ["post"])
def see_survey_result():
    return render_template("info.html", name = request.form['name'], gender = request.form['gender'], location = request.form['location'], fav_language = request.form['fav_language'], improvements = request.form['improvements'], comment = request.form['comment'])


if __name__ == "__main__":
    app.run(debug=True)

