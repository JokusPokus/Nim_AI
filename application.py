from flask import Flask, render_template, url_for, request, session, make_response, jsonify
from flask_session import Session
import nim_gameplay as ngp
import time

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
    ngp.train_and_initialize(session, request.form.get(
        "n_train"), board=INITIAL_BOARD.copy())
    time.sleep(3)
    return render_template("nim.html",
                           new_board=session["current_board"],
                           winner=session["winner"])


@app.route("/ai_move", methods=["POST"])
def ai_move():
    for i in range(len(session["current_board"])):
        # Form input will only be non-empty for the selected row
        if request.form.getlist(f"row_{i}"):
            player_pile = i
            player_amount = len(request.form.getlist(f"row_{i}"))
    print("Player move: " + str(player_pile) + " " + str(player_amount))
    ai_pile, ai_amount = ngp.ai_move(session, player_pile, player_amount)
    print("MOVE: Pile " + str(ai_pile) + " Amount " + str(ai_amount))
    return jsonify(winner=session["winner"], pile=ai_pile, amount=ai_amount)


@app.route("/reset", methods=["GET"])
def reset():
    ngp.reset_board(session, board=INITIAL_BOARD.copy())
    return render_template("nim.html",
                           new_board=session["current_board"],
                           winner=session["winner"])
