from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('project_1a.html')

@app.route("/about")
def about():
    return render_template('project_1b.html')


if __name__ == "__main__":
    app.run(debug=True)