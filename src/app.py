from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def site_root():
    return render_template("login.html")

@app.route('/login')
def log_user():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()