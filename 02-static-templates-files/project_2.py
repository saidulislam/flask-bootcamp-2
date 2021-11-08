"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("project_2a.html")


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("project_2b.html")



if __name__ == "__main__":
    app.run(debug=True)
