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

@app.route("/faq")
def faq():
    return render_template("faq.html")


# Department routes

@app.route("/cs")
def cs():
    return render_template("cs.html")

@app.route("/aerospace")
def aerospace():
    return render_template("aerospace.html")

@app.route("/agri")
def agri():
    return render_template("agri.html")

@app.route("/biotechnology")
def biotechnology():
    return render_template("biotechnology.html")

@app.route("/chemical")
def chemical():
    return render_template("chemical.html")

@app.route("/chemistry")
def chemistry():
    return render_template("chemistry.html")

@app.route("/civil")
def civil():
    return render_template("civil.html")

@app.route("/electrical")
def electrical():
    return render_template("electrical.html")

@app.route("/ece")
def ece():
    return render_template("ece.html")

@app.route("/geology")
def geology():
    return render_template("geology.html")

@app.route("/humanities")
def humanities():
    return render_template("humanities.html")

@app.route("/industrial")
def industrial():
    return render_template("industrial.html")

@app.route("/mathematics")
def mathematics():
    return render_template("mathematics.html")

@app.route("/mechanical")
def mechanical():
    return render_template("mechanical.html")

@app.route("/metallurgy")
def metallurgy():
    return render_template("metallurgy.html")

@app.route("/mining")
def mining():
    return render_template("mining.html")

@app.route("/oena")
def oena():
    return render_template("oena.html")

@app.route("/physics")
def physics():
    return render_template("physics.html")


# Department Professor Routes

@app.route("/cs-001")
def cs001():
    return render_template("cs-001.html")

# Student Routes

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

app.run(debug=True, host='0.0.0.0', port=80)