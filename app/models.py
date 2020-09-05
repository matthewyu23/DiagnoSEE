from flask_sqlalchemy import SQLAlchemy
from config import app
from datetime import datetime


db = SQLAlchemy(app)

class User(db.Model):
    """
    - id (int)
    - name (String) - first and last name
    - username (String)
    - password (String - hash) 
    - define the user as a physician/patient (User)
    """

class Video(db.Model):
    """
    - id (int)
    - user (int) - user id
    - filepath (String) - limit video time to (10~15 seconds) to reduce
    computation time. One user can have multiple rows in the video
    db if they have submitted multiple videos.
    - comment (String) - physician comment
    """
    pass
