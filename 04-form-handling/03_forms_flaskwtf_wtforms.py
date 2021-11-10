from flask import Flask, render_template
from forms3 import LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '678956743562qwetryuFASDF3245234523sdfgsdfgsdfgghjkrty'

users = {
    "john.smith@email.com": "Secret01",
    "rick.taylor@email.com": "Secret02"
}

@app.route("/")
def home():
    return render_template("home3.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login3.html", form = form)

if __name__ == "__main__":
    app.run(debug=True)