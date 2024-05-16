from flask import Flask, request, redirect, render_template, render_template_string, jsonify
from flask.helpers import url_for
from dotenv import load_dotenv
from collections import Counter

import os
import json, requests

app = Flask("DCODE")
app.secret_key = "harshu"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/user-profile")
def user_profile():
    return render_template("users-profile.html")


app.run(debug=True)