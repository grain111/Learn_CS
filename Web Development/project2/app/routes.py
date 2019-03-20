from flask import Flask, render_template, session, request, jsonify, redirect, url_for

from app import app, socketio

import os, datetime

users = {}
channels = {}

max_capacity = 100


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
    channel_name = data["channel_name"]
    if channel_name not in channels:
        channels[channel_name] = []
        socketio.emit("new_channel", channel_name)
    else:
        socketio.emit("error", "Channel name taken!")


@socketio.on("send_message")
def add_message(data):
    message = data["message"]
    channel = data["channel"]
    user = session["user_name"]
    if len(channels[channel]) == max_capacity:
        channels[channel].pop(0)
    channels[channel].append(
        {
            "message": message,
            "user": user,
            "channel": channel,
            "timestamp": datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"),
        }
    )
    socketio.emit("new_message", channels[channel][-1], broadcast=True)


@socketio.on("fetch_channels")
def fetch_channels():
    print("Active channels: {}".format(channels))
    return list(channels.keys())


@socketio.on("fetch_messages")
def fetch_messages(channel):
    return channels[channel]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reset")
def reset():
    users.pop(session["user_name"])
    session.clear()
    return redirect(url_for("index"))
