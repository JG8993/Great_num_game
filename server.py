from flask import Flask, render_template, redirect, session, request
import random
app= Flask(__name__)
app.secret_key = 'larry bird'

@app.route('/')
def index():
    if "number"not in session:
        session["number"] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    if "attempts" not in session:
        session['attempts'] = 0
    else:
        session['attempts'] +=1
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/leaderboard', methods=['POST'])
def leaderboard():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    return render_template("leaderboard.html")

@app.route('/destroy')
def destroy():
    session.clear()
    return redirect('/')

if __name__==("__main__"):
    app.run(debug=True)