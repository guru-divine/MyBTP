from flask import Flask, request, redirect, render_template, render_template_string, jsonify
from flask.helpers import url_for
from dotenv import load_dotenv
from collections import Counter

import os
import json, requests

app = Flask("MyBTP")
app.secret_key = "harshu"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/profile")
def user_profile():
    return render_template("users-profile.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/message")
def message():
    return render_template("register.html")

@app.route("/notification")
def notification():
    return render_template("register.html")

@app.route("/setting")
def setting():
    return render_template("users-profile.html")

@app.route("/cs")
def cs():
    return render_template("cs.html")

@app.route("/cs-001")
def cs001():
    return render_template("cs-001.html")

@app.route("/student")
def student():
    return render_template("student.html")

@app.route("/student_list")
def student_list():
    return render_template("student_list.html")

# Catch-all route for any other URL
@app.route("/<path:path>")
def catch_all(path):
    return render_template("pages-error-404.html")

app.run(debug=True)