import os
import sqlite3
from flask import Flask, render_template, request, session, redirect, flash, g

# Configure application
app = Flask(__name__)

db = sqlite3.connect("qrvwebsite.db", check_same_thread=False)

cursor=db.cursor()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/packages")
def packages():
    return render_template("packages.html")


@app.route("/schedule", methods=["GET", "POST"])
def schedule():
    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        address = request.form.get("address")
        rv_length = request.form.get("rv_length")
        message = request.form.get("message")
        cursor.execute("INSERT INTO customers(name, phone, email, address, rv_length, message) VALUES (?, ?, ?, ?, ?, ?)", (name, phone, email, address, rv_length, message))
        db.commit()
        return render_template("schedule.html")
    else:
        return render_template("schedule.html")


@app.route("/about_us")
def about_us():
    return render_template("about_us.html")