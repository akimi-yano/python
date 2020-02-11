import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    win_patterns = {"paperrock": "You win!", "rockscissors": "You win!", "scissorspaper": "You win!"}
    random_num = random.randint(0,2)
    choices_p2 =["paper", "rock", "scissors"]
    p2 = choices_p2[random_num]
    p1 = request.form['pick']
    if p1==p2:
        result = "It's a tie!"
    elif p1+p2 in win_patterns:
        result = win_patterns[p1+p2]
    else:
        result = "You lose!"
    return render_template('results.html',p1=p1,p2=p2,result=result)

if __name__ == "__main__":
    app.run(debug=True)
