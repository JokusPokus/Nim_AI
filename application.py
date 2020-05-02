from flask import Flask, render_template, url_for, request, session, make_response
from flask_session import Session
from nimAI import train, play

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

INITIAL_BOARD = [1, 3, 5, 7]


@app.route("/")
def index():
    print("Hey from index")
    return render_template("index.html")


@app.route("/nim", methods=["GET", "POST"])
def nim():
    if request.method == "GET":
        if not session.get("current_board"):
            session["n_train"] = None
        session["current_board"] = INITIAL_BOARD
    else:
        if "n_train" in request.form:
            session["n_train"] = request.form.get("n_train")
        if "pile" in request.form:
            pile = request.form.get("pile")
        if "amount" in request.form:
            amount = request.form.get("amount")
            session["current_board"][int(pile) - 1] -= min(int(amount), session["current_board"][int(pile) - 1])

    return render_template("nim.html", n_train=session["n_train"], new_board=session["current_board"])

