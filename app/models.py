from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
from datetime import datetime
from application import db


class User(db.Model):
    """
    - id (int)
    - name (String) - first and last name
    - username (String)
    - password (String - hash) 
    - define the user as a physician/patient (User)
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    fullname = db.Column(db.String, nullable=False) 
    password = db.Column(db.String, nullable=False) 
    is_patient = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f'<User {self.username} - {"Patient" if self.is_patient else "Physician"}>'

class Video(db.Model):
    """
    - id (int)
    - user (int) - user id
    - filepath (String) - limit video time to (10~15 seconds) to reduce
    computation time. One user can have multiple rows in the video
    db if they have submitted multiple videos.
    - comment (String) - physician comment
    """
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, nullable=False)
    physician_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String)
    filepath_old = db.Column(db.String)
    filepath_new = db.Column(db.String)

    def __repr__(self):
        return f'<Video {self.id} - Patient ({self.patient_id}) Physician ({self.physician_id})>'




