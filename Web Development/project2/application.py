from flask import Flask, render_template, session, request, jsonify, redirect, url_for
from flask_session import Session

app = Flask(__name__)
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add_user", methods=["POST"])
def add_user():
    session["user_name"] = request.form.get("user_name")
    return jsonify({"result": "success"})

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for('index'))
