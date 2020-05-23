from flask import Flask, render_template, url_for, request, session, make_response
from flask_session import Session
import nim_gameplay as ngp

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

INITIAL_BOARD = [1, 3, 5, 7]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/nim_train", methods=["GET"])
def nim_train():
    return render_template("nim_train.html")


@app.route("/nim", methods=["POST"])
def nim():
    # When training is requested (via POST request)
    ngp.train_and_initialize(session, request.form.get("n_train"), board=INITIAL_BOARD.copy())
    return render_template("nim.html",
                           new_board=session["current_board"],
                           winner=session["winner"])


@app.route("/nim_move", methods=["GET"])
def nim_move():
    # When resetting game
    if request.args.get("status") == "reset":
        ngp.reset_board(session, board=INITIAL_BOARD.copy())

    # When player makes a move
    if request.args.get("pile"):
        ngp.player_move(session, pile=request.args.get("pile"), amount=request.args.get("amount"))

    # If game still going: Calculate an AI move
    # If game over: Show result
    if request.args.get("status") == "ai_move":
        ngp.ai_move(session)

    return render_template("nim_board.html", winner=session["winner"], new_board=session["current_board"])


@app.route("/reset", methods=["GET"])
def reset():
    ngp.reset_board(session, board=INITIAL_BOARD.copy())
    return render_template("nim.html",
                           new_board=session["current_board"],
                           winner=session["winner"])