from flask import (Flask, render_template, request, jsonify, redirect, url_for, flash)
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    taskname = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    duration = db.Column(db.String)
    count = db.Integer()
    timeperiod = db.Integer()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')