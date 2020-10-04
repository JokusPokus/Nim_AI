from ..nim_gameplay import train_and_initialize
from ..nimAI import NimAI


class TestTrainAndInitialize:
    def test_produce_nimai_instance():
        session = dict()
        n_train = 100
        board = [1, 3, 5, 7]
        train_and_initialize(session, n_train, board)
        assert isinstance(session["nim_ai"], NimAI)


