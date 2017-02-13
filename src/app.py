from flask import Flask, render_template, request, session

from src.common.Database import Database
from src.models.User import User

app = Flask(__name__)
app.secret_key = "joeyplus"

@app.route('/login')
def log_in():
    return render_template("login.html")

@app.route('/register')
def register_user():
    return render_template("signup.html")

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/auth/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    name = User.name

    if User.is_login_valid(email, password):
        User.login(name, email)

    return render_template("dashboard.html", email=session['email'], name=session['name'])


@app.route('/auth/signup', methods=['POST'])
def signUpUser():
    return render_template("signup.html")

if __name__ == '__main__':
    app.run()