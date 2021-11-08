from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the homepage!"

@app.route("/store")
def store():
    return "Welcome to my store!"

if __name__ == "__main__":
    app.run(debug=True)