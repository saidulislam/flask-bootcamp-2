from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitest.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Student(db.Model):
    roll_number = db.Column(db.Integer, primary_key = True, unique = True)
    name = db.Column(db.String, nullable = False)
    batch = db.Column(db.String, nullable = False)


db.create_all()

# STEP 1: create the user object
stu1 = Student(name = "Romanah", batch = "2015")
stu2 = Student(name = "Smith", batch = "2015")
stu3 = Student(name = "Joan", batch = "2016")
stu4 = Student(name = "Barbarah", batch = "2018")

# STEP 2: add the user to the database
db.session.add(stu1)
db.session.add(stu2)
db.session.add(stu3)
db.session.add(stu4)

# STEP 3: commit the change to the database
try:
    db.session.commit()
except Exception as e: 
    db.session.rollback()
finally:
    db.session.close()

ah_student = Student.query.filter_by(batch='2015').filter(Student.name.endswith('ah')).first()
print(ah_student.name)