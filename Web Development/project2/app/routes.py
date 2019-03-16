from flask import Flask, render_template, session, request, jsonify, redirect, url_for

from app import app, socketio

import os

users = {}
channels = {}


@socketio.on("connect")
def handle_message():
    print("User connected " + request.sid)
    if "user_name" in dict(session):
        users[dict(session)["user_name"]] = request.sid
    print(users)


@socketio.on("disconnect")
def handle_message():
    print("User disconnected " + request.sid)


@socketio.on("login")
def login(name):
    user_name = name["name"]
    if user_name not in users:
        users[user_name] = request.sid
        session["user_name"] = user_name
        socketio.emit("login_success", render_template("chat.html"))
    else:
        socketio.emit("error", "User name taken!")

@socketio.on("add_channel")
def add_channel(data):
    if data["channel_name"] not in channels:
        channels[data["channel_name"]] = []
        print(data)
    else:
        socketio.emit("error", "Channel name taken!")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reset")
def reset():
    users.pop(session["user_name"])
    session.clear()
    return redirect(url_for("index"))
