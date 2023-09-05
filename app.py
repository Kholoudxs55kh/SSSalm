"""importing modules
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """home page
    """
    return render_template("index.html")

@app.route("/lovelySalma")
def salma_function():
    """Salma's
    """
    return render_template("Salma.html")