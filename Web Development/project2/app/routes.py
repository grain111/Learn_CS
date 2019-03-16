from flask import Flask, render_template, session, request, jsonify, redirect, url_for

from app import app, socketio

import os

users = {}

@socketio.on('connect')
def handle_message():
    print("User connected " + request.sid)
    if dict(session)["user_name"]:
        users[dict(session)["user_name"]] = request.sid
    print(users)

@socketio.on('disconnect')
def handle_message():
    print("User disconnected " + request.sid)

@socketio.on('login')
def login(name):
    user_name = name["name"]
    if user_name not in users:
        users[user_name] = request.sid
        session["user_name"] = user_name
        print(users)
        socketio.emit("login_success", render_template("chat.html"))
    else:
        socketio.emit("error", "User name taken!")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))
