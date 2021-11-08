from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    Users = {
                "user 1":"John Smith", 
                "user 2":"Derek Smith", 
                "user 3":"Bob Walsh", 
                "user 4":"Rick Taylor",
                "user 5":"Admin"
            }
    return render_template("index3.html", users=Users)


if __name__ == "__main__":
    app.run(debug=True)