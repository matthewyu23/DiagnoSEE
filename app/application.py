import os

from flask import Flask, session, render_template, request, url_for, jsonify, redirect, flash
# from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_socketio import SocketIO, emit
import requests
from json import load, dumps
from werkzeug.utils import secure_filename


# sets up environment and db
app = Flask(__name__)
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register.html")
def register():
    return render_template("register.html")

@app.route("/validate_user", methods=["POST"])
def val_user():
    full_name = request.form.get("full_name")
    username = request.form.get("user")
    password = request.form.get("password")
    is_patient = request.form.get("user_type")
    if db.execute("SELECT * FROM users WHERE username = :username", {"username":username}).rowcount == 0:
        db.execute("INSERT INTO users (full_name, username, password, is_patient) VALUES (:full_name, :username, :password, :is_patient)", {"full_name":full_name, "username":username, "password":password, "is_patient":is_patient})
        db.commit()
        return render_template("index.html")
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
    try:
        username = session["username"]
        user_info = db.execute("SELECT * FROM users WHERE username = :username",
                             {"username", username}).fetchone()
        is_patient = user_info['is_patient']
        if is_patient:
            videos = db.execute("SELECT * FROM videos WHERE patient_id = :user_id",
                                {"user_id": user_info['user_id']}).fetchall()
        else:
            videos = db.execute("SELECT * FROM videos WHERE physician_id = :user_id",
                                {"user_id": user_info['user_id']}).fetchall()
        return render_template("view_video.html", user_info=user_info, videos=videos)
    except:
        return '''
                <html>
                    <h1>You did not login!</h1>
                </html>
                '''
@app.route("/chat.html")
def chat():
    return render_template("chat.html")

@app.route("/channels", methods=["POST"])
def channels():
    channel = request.form.get("chan")
    msg[channel] = []
    if channel not in channels_list:
        channels_list.append(channel)
        return jsonify({"error":False, "new_channel":channel})
    else:
        return jsonify({"error":True})

@app.route("/populate_channels")
def populate_channels():
    return jsonify({"chans":json.dumps(channels_list)})

@app.route("/<string:channel_name>.html")
def in_channel(channel_name):
    print("I am sending you to a channel")
    msgs = msg[channel_name]
    return render_template("channel.html", msgs=msgs, channel_name=channel_name)

app.config['ALLOWED_EXTENSIONS'] = ['mp4']
app.config['UPLOAD_FOLDER'] = 'nets/'
def allowed_files(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part.')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if not allowed_files(file.filename):
            flash('File type not supported! Please upload a file with extension ' + ','.join(app.config['ALLOWED_EXTENSIONS']))
            return render_template("upload.html")
        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # adding video into the database for later
            # i = Image(filename=filename)
            # db.session.add(i)
            # call function that runs the neural network
            # redirect the user to the result of the network
            return redirect(url_for('view_video',
                                        filename=filename))
    else:
        return render_template("upload.html")

@app.route('/view_video/<filename>')
def view_video(filename):
    return render_template("view_video.html")

@socketio.on("submit message")
def message(data):
    print("at submit message")
    username = data["username"]
    message = data["message"]
    timestamp = datetime.now()
    channel = data["channel"]
    ts = str(timestamp)
    msg[channel].append([username, message, timestamp])
    if len(msg[channel]) == 101:
        msg[channel].pop(0)
    print(msg)
    emit('announce message', {'channel': channel, 'username': username, 'message': message, 'timestamp': ts}, broadcast=True)

if __name__ == '__main__':
    app.run()