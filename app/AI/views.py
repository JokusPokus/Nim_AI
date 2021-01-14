import time
from flask import render_template, request, session, jsonify, current_app
from . import ai
from ..AI.nim_gameplay import (train_and_initialize,
                               update_game_state,
                               ai_lost,
                               ai_move,
                               declare_human_winner,
                               update_high_score)


@ai.route("/train", methods=["GET"])
def show_training_options():
    """
    Render training page,
    allowing user to select the amount of AI training rounds
    """
    session["high_score"] = session.get("high_score", 0)
    return render_template("nim_train.html",
                           high_score=session["high_score"])


@ai.route("/nim", methods=["POST"])
def train_and_show_board():
    """
    Train AI agent
    and render game-playing page with initialized board
    """
    # Training with n_train rounds is requested
    n_train = int(request.form.get("n_train"))

    # BE validation to avoid malicious post requests
    # (n_train cannot be set to > 300 by using FE functionality)
    if n_train > 300:
        exit()

    # The input slider is not linear.
    # For higher numbers, one slider unit increases n_train quicker.
    if n_train > 200:
        n_train = 1000 + (n_train - 200) * 90
    elif n_train > 100:
        n_train = 100 + (n_train - 100) * 9

    session["n_train"] = n_train
    session["high_score"] = session.get("high_score", 0)

    train_and_initialize(session, n_train, board=current_app.config["INITIAL_BOARD"].copy())
    time.sleep(2.9)
    return render_template("nim.html",
                           new_board=session["current_board"],
                           winner=session["winner"],
                           high_score=session["high_score"])


@ai.route("/ai_move", methods=["POST"])
def send_ai_move():
    """
    Update board state representation.
    Request an AI move and send it back to client as JSON.
    Requests are managed via AJAX.
    """
    def get_player_move(session, request):
        pile = amount = None
        for i in range(len(session["current_board"])):
            # Form input will only be non-empty for the selected row
            if request.form.getlist(f"row_{i}"):  # e.g., ["Clicked", "Clicked", "Clicked]
                pile = i
                amount = len(request.form.getlist(f"row_{i}"))
        return pile, amount

    # Player's move
    player_pile, player_move = get_player_move(session, request)
    update_game_state(session, player_pile, player_amount)

    # AI's move
    ai_pile, ai_amount = ai_move(session)
    update_game_state(session, ai_pile, ai_amount)

    if ai_lost(session["current_board"]):
        declare_human_winner(session)
        update_high_score(session)

    return jsonify(winner=session["winner"],
                   pile=ai_pile,
                   amount=ai_amount,
                   high_score=session["high_score"])
