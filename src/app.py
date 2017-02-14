from flask import Flask, render_template, request, session

from src.common.Database import Database
from src.models.User import User

app = Flask(__name__)
app.secret_key = "joeyplus"


@app.route('/register')
def register_user():
    return render_template("signup.html")

@app.route('/dashboard')
def display_dsshboard():
    return render_template("dashboard.html")

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
        return render_template("dashboard.html")
    else:
        return render_template("login.html")

@app.route('/auth/signup', methods=['GET'])
def display_signin():
    return render_template("login.html")

@app.route('/auth/signup', methods=['POST'])
def signUpUser():
    return render_template("signup.html")

if __name__ == '__main__':
    app.debug = True
    app.run()