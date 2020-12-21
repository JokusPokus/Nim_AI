from app.AI.train import train


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


def ai_move(session, pile, amount):
    """
    Updates the current board according to the Human's move and picks the AI's response.
    If the Human has already lost before the AI move or the AI loses after its move,
    session["winner"] is updated.
    """
    pile = int(pile)
    amount = int(amount)

    # Take chosen amount of objects from the pile
    session["current_board"][pile] -= amount

    # Get AI move and update board
    pile, amount = session["nim_ai"].choose_action(session["current_board"], epsilon=False)
    session["current_board"][pile] -= amount

    # If AI lost the game
    if not any(session["current_board"]):
        session["winner"] = "Human"
        session["high_score"] = max(session["n_train"], session["high_score"])

    return pile, amount

