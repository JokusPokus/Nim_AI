from flask import Flask, render_template, url_for, request
from nimAI import train, play

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nim", methods=["GET", "POST"])
def nim():
    if request.method == "GET":
        word = None
    else:
        word = request.form.get("word")
    return render_template("nim.html", word=word)
