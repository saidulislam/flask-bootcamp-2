from flask import Flask, render_template
from forms4 import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wertxdfgjhdvjk4567123454567sgqwe43576youi34tgfd56781234dghf'

users = {
    "john.smith@email.com": "secret01",
    "rick.smith@email.com": "secret02"
}

@app.route("/")
def home():
    return render_template("home4.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.is_submitted():
        print("Submitted.")
    
    if form.validate():
        print("Valid.")

    if form.validate_on_submit():
       print("Submitted and Valid.")

    return render_template("login4.html", form = form)

if __name__ == "__main__":
    app.run(debug=True)