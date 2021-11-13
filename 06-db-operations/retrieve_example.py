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

# STEP 1: create the user object
archie = User(email = "archie.andrews@email.com", password = "football4life")
veronica = User(email = "veronica.lodge@email.com", password = "fashiondiva")

# STEP 2: add the user to the database
db.session.add(archie)
db.session.add(veronica)

# STEP 3: commit the change to the database
try:
    db.session.commit()
except Exception as e: 
    db.session.rollback()
finally:
    db.session.close()

# STEP 4: retrieve the object
# query.all()
print(User.query.all())

# query.first()
print(User.query.first())

# query.get()
user = User.query.get('veronica.lodge@email.com')
print(user)
print(user.email)
print(user.password)

# query.filter_by()
user = User.query.filter_by(password="football4life")
print(user) # Query Object - prints the sql query
print('*'*20)

## Add first() Method to Retrieve the First Result from Query
user = User.query.filter_by(password = "football4life").first()
print(user)
print(user.email)
print(user.password)

## 
# ****** query.filter() ******
# contains()
# endswith()
# startswith()
# like()
##
print('----------------')
print('query.filter()')
user = User.query.filter(User.email == "veronica.lodge@email.com")
print(user) #Base Query Object
print('*'*20)

# Add first() Method to Retrieve the First Result from Query
user = User.query.filter(User.email == "veronica.lodge@email.com").first()
print(user)
print('*'*20)

# A Query with Multiple Expressions
user = User.query.filter(User.email == "archie.andrews@email.com", User.password.contains("anonpass"))
print(user)
print('*'*20)
print(user.first())


