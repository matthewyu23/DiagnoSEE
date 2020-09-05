import os
import flask
import Flask, render_template, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


@app.route('/home')
def index():
    """
    The homepage of the website,
    render application templates.
    """
    return


@app.route('/client')
def client_home():
    """
    The homepage of the patients,
    render application templates.
    """
    return

@app.route('/client/add', methods=['POST'])
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
