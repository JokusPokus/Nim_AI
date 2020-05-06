from nimAI import train


def train_and_initialize(session, n_train, board):
    """
    Trains the agent for n_train rounds and initializes the board.
    Everything is saved in the sessions dictionary.
    """
    session["nim_ai"] = train(int(n_train))
    session["current_board"] = board
    session["winner"] = 0  # no winner yet


def reset_board(session, board):
    """
    Resets the board to its initial state with no winner.
    """
    session["current_board"] = board
    session["winner"] = 0  # no winner yet


def player_move(session, pile, amount):
    """
    Updates the current board according to the Human's move
    """
    pile = int(pile)
    amount = int(amount)

    # Take chosen amount of objects from the pile
    # (but don't allow negative amounts)
    session["current_board"][pile - 1] -= min(amount, session["current_board"][pile - 1])


def ai_move(session):
    """
    Requests an AI move and updates the current board.
    If the Human has already lost before the AI move or the AI loses after its move,
    session["winner"] is updated.
    """
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
