from flask import Flask, render_template, url_for, request, session, make_response
from flask_session import Session
from nimAI import train

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
    session["n_train"] = int(request.form.get("n_train"))
    session["nim_ai"] = train(session["n_train"])
    session["current_board"] = INITIAL_BOARD.copy()
    session["winner"] = 0  # no winner yet

    return render_template("nim.html",
                           new_board=session["current_board"],
                           winner=session["winner"])


@app.route("/nim_move", methods=["GET"])
def nim_move():
    # When resetting game
    if request.args.get("status") == "reset":
        session["current_board"] = INITIAL_BOARD.copy()
        session["winner"] = 0  # no winner yet

    # When player makes a move
    if request.args.get("pile"):
        pile = int(request.args.get("pile"))
        amount = int(request.args.get("amount"))

        # Take chosen amount of objects from the pile
        # (but don't allow negative amounts)
        session["current_board"][pile - 1] -= min(amount, session["current_board"][pile - 1])

    # Calculate an AI move if requested and game still going
    if request.args.get("status") == "ai_move":

        # If Human has already lost
        if not any(session["current_board"]):
            session["winner"] = "AI"

        # If game is still going on
        else:
            pile, amount = session["nim_ai"].choose_action(session["current_board"], epsilon=False)

            # Update board based on AI move
            session["current_board"][pile] -= amount
            print(session["current_board"])

            # If AI lost the game
            if not any(session["current_board"]):
                session["winner"] = "Human"

    return render_template("nim_board.html",
                           winner=session["winner"],
                           new_board=session["current_board"])
