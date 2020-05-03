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
        # If page is requested before training
        if request.args.get("status") == "before":
            session["n_train"] = None
            session["nim_ai"] = None
            session["current_player"] = None
            session["current_board"] = INITIAL_BOARD

        # When resetting game
        session["current_player"] = 0  # Human
        session["current_board"] = INITIAL_BOARD

        # Calculate an AI move if requested
        if request.args.get("move") == "ai":
            print("Yippie Yeah")
            pile, amount = session["nim_ai"].choose_action(session["current_board"], epsilon=False)

            # Update board based on AI move
            session["current_board"][pile] -= amount

            # Change current player to Human
            session["current_player"] = 0

    else:
        print("POST requesssst")
        # When training is requested
        if "n_train" in request.form:
            print("Yippie")
            session["n_train"] = int(request.form.get("n_train"))
            session["nim_ai"] = train(session["n_train"])

            # Human starts
            session["current_player"] = 0

        # When player makes a move
        if "pile" in request.form:
            pile = int(request.form.get("pile"))
        if "amount" in request.form:
            amount = int(request.form.get("amount"))

            # Take chosen amount of objects from the pile
            # (but don't allow negative amounts)
            session["current_board"][pile - 1] -= min(amount, session["current_board"][pile - 1])

            # Change current player to AI
            session["current_player"] = 1

    return render_template("nim.html",
                           is_trained=bool(session["nim_ai"]),
                           new_board=session["current_board"])

