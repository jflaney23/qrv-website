import os
from flask import Flask, render_template, request, session, redirect, flash

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/packages")
def packages():
    return render_template("packages.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/about_us")
def about_us():
    return render_template("about_us.html")