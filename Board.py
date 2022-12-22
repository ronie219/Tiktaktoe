from copy import deepcopy


class Board:

    def __init__(self, size: int):
        self.size = size
        self.board = []
        for _ in range(size):
            self.board.append(deepcopy([None] * size))
