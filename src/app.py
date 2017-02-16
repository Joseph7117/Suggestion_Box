import random

import datetime
from flask import Flask, render_template, request, session, redirect, url_for
from flask import flash

from src.common.Database import Database
from src.models.Reactions import Reactions
from src.models.User import User
from src.models.Suggestion import Suggestions

app = Flask(__name__)
app.secret_key = "joeyplus"


@app.route('/register')
def register_user():
    return render_template("signup.html")

@app.route('/dashboard')
def display_dashboard():
    suggestions = Suggestions.fetch_suggestions()
    if session['email'] is None:
        return redirect(url_for('login_user'))
    return render_template("dashboard.html", suggestions=suggestions)

@app.route('/reactions/<q>', methods=['GET'])
def reactions_display(q=None):
    q = int(q)
    reactions = Suggestions.fetch_reaction(q)
    suggest = Suggestions.fetch_by_id(q)
    if session['email'] is None:
        return redirect(url_for('login_user'))
    return render_template("reactions.html", reactions=reactions, suggest=suggest)

@app.route('/reactions', methods=['POST'])
def add_reaction():
    suggestions_id = request.form['suggest_id']
    comment = request.form['comments-area']
    email = session['email']
    date = datetime.datetime.utcnow()
    upvote = request.form.getlist('upvoting')
    downvote = request.form.getlist('downvoting')
    flagging = request.form.getlist('flagging')

    react = Reactions(suggestions_id, email, comment, date, upvote, downvote, flagging)
    react.save_to_db()

    flash("Thank you for the reaction we shall scrutinize your view")

    return redirect(url_for('display_dashboard'))

@app.before_first_request
def init_db():
    Database.initialize()

@app.route('/auth/login', methods=['GET'])
def auth_form():
    return render_template("login.html")

@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    validate = User.is_login_valid(email, password)
    if validate is True:
        session['email'] = email
        return render_template("dashboard.html", email=email)
    else:
        return render_template("login.html")
@app.route('/logout')
def log_out():
    session['email'] = None
    return redirect(url_for('login_user'))

@app.route('/auth/signup', methods=['GET'])
def display_signin():
    return render_template("signup.html")

@app.route('/auth/signup', methods=['POST'])
def signUpUser():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    user = User(username, email, password)
    user.save_to_mongo()

    session['email'] = email
    flash("You were Successfully Registered!")

    return redirect(url_for('display_dashboard'))

@app.route('/suggest', methods=['GET'])
def suggestDashboard():
    return render_template('dashboard.html')

@app.route('/suggest', methods=['POST'])
def addSuggest():
    suggestTitle = request.form['suggestion-title']
    description = request.form['suggestion-description']
    email = session['email']
    board_id = random.randint(1, 100)

    suggest = Suggestions(board_id, email, suggestTitle, description)
    suggest.save_to_db()

    flash("You Successfully Added a Suggestion")

    return redirect(url_for('display_dashboard'))



if __name__ == '__main__':
    app.debug = True
    app.run()