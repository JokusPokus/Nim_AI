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
    return render_template("index.html")


@app.route("/nim", methods=["GET", "POST"])
def nim():
    if request.method == "GET":
        # When page is requested before training
        if request.args.get("status") == "before":
            session["n_train"] = None
            session["nim_ai"] = None
            session["winner"] = 0  # no winner yet
            session["current_board"] = INITIAL_BOARD

        # When resetting game
        if request.args.get("status") == "reset":
            session["current_board"] = INITIAL_BOARD
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

    else:

        # When training is requested
        if "n_train" in request.form:
            session["n_train"] = int(request.form.get("n_train"))
            session["nim_ai"] = train(session["n_train"])

    return render_template("nim.html",
                           is_trained=bool(session["nim_ai"]),
                           new_board=session["current_board"],
                           winner=session["winner"])
