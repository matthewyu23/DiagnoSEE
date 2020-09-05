import os
import flask
import Flask, render_template, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


@app.route('/')
def index():
    """
    The homepage of the website,
    render application templates.
    """
    return
