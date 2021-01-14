from flask import render_template, request, session, jsonify, current_app

from . import main

from ..AI import nim_gameplay as ngp


@main.route("/")
def index():
    """
    Render landing page with the options to
    - expand and read the rules
    - select training options
    """
    session["high_score"] = session.get("high_score", 0)
    return render_template("index.html",
                           high_score=session["high_score"])


@main.route("/reset", methods=["GET"])
def reset():
    """
    Reset the board without training the AI agent again.
    """
    ngp.reset_board(session, board=current_app.config["INITIAL_BOARD"].copy())
    return render_template("nim.html",
                           new_board=session["current_board"],
                           winner=session["winner"],
                           high_score=session["high_score"])
