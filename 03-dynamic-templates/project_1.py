"""Flask Application for Paws Rescue Center."""
from flask import Flask, render_template, abort
app = Flask(__name__)

"""Information regarding the Pets in the System."""
pets = [
            {"id": 1, "name": "Nelly", "age": "5 weeks", "bio": "I am a tiny kitten rescued by the good people at Paws Rescue Center. I love squeaky toys and cuddles."},
            {"id": 2, "name": "Yuki", "age": "8 months", "bio": "I am a handsome gentle-cat. I like to dress up in bow ties."},
            {"id": 3, "name": "Basker", "age": "1 year", "bio": "I love barking. But, I love my friends more."},
            {"id": 4, "name": "Mr. Furrkins", "age": "5 years", "bio": "Probably napping."}, 
        ]

@app.route("/")
def homepage():
    """View function for Home Page."""
    return render_template("project_1_home.html", pets_col=pets)


@app.route("/details/<int:pet_id>")
def details(pet_id):
    """View function for Detail Page."""
    pet = next((pet for pet in pets if pet["id"] == pet_id), None)
    if pet is None: 
        abort(404, description="No Pet was Found with the given ID")
    return render_template("details.html", pet=pet)


@app.route("/about")
def about():
    """View function for About Page."""
    return render_template("project_1_about.html")


if __name__ == "__main__":
    app.run(debug=True)
