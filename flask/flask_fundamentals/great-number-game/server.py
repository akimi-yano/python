from flask import Flask, render_template, request, redirect, session
import random 

app = Flask(__name__)

app.secret_key = "secret_key"

@app.route('/')
def take_a_guess():
    if 'answer' not in session:
        session['answer'] = random.randint(0, 100)
        session['decision'] = ''
        session['color'] = ''
        session['counter'] = 0
    if 'leaderboard' not in session:
        session['leaderboard'] = {}
    return render_template('index.html', answer = session['answer'], decision = session['decision'], color = session['color'], counter = session['counter'], leaderboard = session['leaderboard'])


@app.route('/judge', methods = ['POST'])
def  judge():
    input_answer = int(request.form['number'])
    answer = session['answer']
    session['counter'] +=1
    if input_answer == answer:
        session['decision'] = "Correct!"
        session['color'] = 'green'
    elif input_answer > answer:
        session['decision'] = 'Too High'
        session['color'] = 'red'
    elif input_answer < answer:
        session['decision'] = 'Too Low'
        session['color'] = 'red'
    print("Shhhh... the answer is " + str(session['answer']))
    return redirect("/")

@app.route('/reset')
def reset():
    temp = session['leaderboard']
    session.clear()
    session['leaderboard'] = temp
    return redirect('/')

@app.route('/leaderboard', methods = ['POST'])
def leaderboard():
    name = request.form['name']

    # Flask uses immutable dictionary, so cannot directly modify the leaderboard dict.
    # session['leaderboard'][name] = session['counter']
    leaderboard_dict = session['leaderboard']
    leaderboard_dict[name] = session['counter']
    session['leaderboard'] = leaderboard_dict

    return redirect("/")
        
if __name__ == "__main__":
    app.run(debug = True)