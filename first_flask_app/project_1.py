"""Flask Application for Paws Rescue Center."""
from flask import Flask

app = Flask(__name__)


"""1. Add a View Function for the Home page."""
@app.route("/")
def home():
    return "Paws Rescue Center 🐾"    

"""2. Add a View Function for the About page."""
@app.route("/about")
def about():
    return "We are a non-profit organization working as an animal rescue. \
        We aim to help you connect with the purrfect furbaby for you! The \
            animals you find on our website are rescued and rehabilitated \
                animals. Our mission is to promote the ideology \"adopt, \
                    don't hop\"! "

if __name__ == "__main__":
    """ """
    app.run(debug=True)
