from flask import Flask, render_template, request, redirect, session
# import base64

app = Flask(__name__)

app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def visits():
    if 'visits' in session:
        session['visits'] = session['visits'] + 1  # reading and updating session data
        session['actual'] += 1
    else:
        session['visits'] = 1 # setting session data
        session['actual'] = 1
    total_visits = session['visits']
    # myvariable = base64.urlsafe_b64decode('eyJhY3R1YWwiOjIsInZpc2l0cyI6NDF9')
    return render_template('index.html', visits = total_visits, actual = session['actual'])
    
@app.route('/destroy_session')
def delete_visits():
    # session.pop('visits', None) # delete visits
    session.clear()
    return redirect('/')

@app.route('/add_two_visits')
def add_two_visits():
    session['visits'] += 1
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment_num():
    session['visits'] += int(request.form['increment_num']) - 1
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
