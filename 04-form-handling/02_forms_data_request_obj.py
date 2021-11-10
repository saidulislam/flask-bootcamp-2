from flask import Flask, render_template
from flask import request

app = Flask(__name__)

users = {
    "john.smith@email.com": "Secret01",
    "rick.taylor@email.com": "Secret02"
}

@app.route("/")
def home():
    return render_template("home2.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email in users and users[email] == password:
            return render_template("login2.html", message ="Successfully Logged In")
        return render_template("login2.html", message ="Incorrect Email or Password")
    return render_template("login2.html")

if __name__ == "__main__":
    app.run(debug=True)