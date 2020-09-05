import os
import flask
import Flask, render_template, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


@app.route('/register')
def register():
    """
    Register user.
    """
    return

@app.route("/validate_user", methods=["POST"])
def val_user():
    """
    authentication patient and physician.
    """
    return

@app.route("/login")
def login():
    return

@app.route("/login/validate")
def val_login():
    return

@app.route('/home')
def index():
    """
    The homepage of the website,
    render application templates.
    """
    return render_template("static/index.html")

@app.route('/patient')
def patient_home():
    """
    The homepage of the patients,
    render application templates.
    """
    return render_template("static/patient.html");

@app.route('/patient/add', methods=['POST'])
def patient_add():
    """
    Interface for patient to add videos.
    render application and redirect client to page where 
    they can view their submissions.
    """ 
    return

@app.route('/doctor')
def doctor_home():
    """
    The homepage of the physicians,
    view patient video submissions.
    """
    return

"""
@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/register.html")
def register():
    return render_template("register.html")

@app.route("/validate_user", methods=["POST"])
def val_user():
    username = request.form.get("user")
    password = request.form.get("password")
    if db.execute("SELECT * FROM users WHERE username = :username", {"username":username}).rowcount == 0:
        db.execute("INSERT INTO users (username, password) VALUES (:username, :password)", {"username":username, "password":password})
        db.commit()
        return render_template("welcome.html")
    else:
        return render_template("register.html", error_message="This username has been taken. Please try a different one.")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/validate_login", methods=["POST"])
def val_login():
    uname = request.form.get("user")
    password = request.form.get("password")
    if db.execute("SELECT * FROM users WHERE username = :username", {"username":uname}).rowcount == 0:
        return render_template("login.html", error_message="This username doesn't exist! Go back to the register page.")
        # check if password for the username exists and matches the input
    pword = ((db.execute("SELECT password FROM users WHERE username = :username", {"username":uname}).fetchall())[0])[0]
    if password == pword:
        session["username"] = uname
        return redirect(url_for("welcome_user", _external=True))
        # return render_template("welcome_user.html")
    return render_template("login.html", error_message="This password is incorrect!")

@app.route("/welcome_user")
def welcome_user():
    return render_template("welcome_user.html")
"""