from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    Username = "Saidul"
    return render_template("index.html", username=Username)


if __name__ == "__main__":
    app.run(debug=True)