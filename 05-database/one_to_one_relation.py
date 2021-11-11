from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    department_name = db.Column(db.String, db.ForeignKey('department.name'), nullable = False)
    is_head_of = db.Column(db.String, db.ForeignKey('department.name'), nullable=True)


class Department(db.Model):
    name = db.Column(db.String(50), primary_key=True, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    employees = db.relationship('Employee', backref='department')
    # **** uselist ****
    # This step in the one-to-one relationship is what differentiates it from a 
    # one-to-many relationship. We need to make sure that this relationship is 
    # not built with more than one employee. Therefore, we will add an extra 
    # argument to the function called useList and set it to False. This will make 
    # sure that it does not point to a list.
    head = db.relationship('Employee', backref='head_of_department', uselist=False)


class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False) 

