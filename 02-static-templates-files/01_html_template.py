from flask import Flask

@app.route("/")
def home():
    return "<h1 align->Welcome to the HomePage!</h1>"


if __name__ == "__main__":
    app.run(debug=True)