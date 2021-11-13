from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    email = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

db.create_all()
db.session.add(User(email = "archie.andrews@email.com", password = "football4life"))
db.session.add(User(email = "veronica.lodge@email.com", password = "fashiondiva"))

try:
    db.session.commit()
except Exception as e:
    db.session.rollback()
    
user = User.query.get("veronica.lodge@email.com")
print(user)

# DELETE the user
db.session.delete(user)

try:
    db.session.commit()
except Exception as e:
    db.session.rollback()

print("All Users : ", User.query.all())
