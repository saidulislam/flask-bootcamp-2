from flask import Flask, render_template
from forms5 import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wertxdfgjhdvjk4567123454567sgqwe43576youi34tgfd56781234dghf'

users = {
    "john.smith@email.com": "secret01",
    "rick.smith@email.com": "secret02"
}

@app.route("/")
def home():
    return render_template("home5.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        for u_email, u_password in users.items():
            if u_email == form.email.data and u_password == form.password.data:
                return render_template("login5.html", message ="Successfully Logged In")
        return render_template("login5.html", form = form, message ="Incorrect Email or Password")
    elif form.errors:
        print(form.errors.items())
    return render_template("login5.html", form = form)

if __name__ == "__main__":
    app.run(debug=True)