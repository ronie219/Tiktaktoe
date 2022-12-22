from Board import Board
from Player import Player
from typing import List
from collections import deque


class Game:

    def __init__(self, players: List[Player], board: Board, size: int):
        self.board = board
        self.players = players
        self.size = size

    @staticmethod
    def _check_coordinate_structure(coordinate: List):
        if len(coordinate) != 2:
            print("please enter a valid request coordinate i.e x,y")
            return False
        return True

    def _check_board_cell(self, coordinate: List):
        if self.board.board[coordinate[0]][coordinate[1]] is not None:
            print("Please enter a valid position as this position is already filled")
            return False
        return True

    def _check_board_boundary(self, coordinate: List):
        flag = True
        if coordinate[0] < 0 or coordinate[0] >= self.size:
            print("Please provide a valid x coordinate")
            flag = False
        if coordinate[1] < 0 or coordinate[1] >= self.size:
            print('Please provide a valid y coordinate')
            flag = False
        return flag

    def _check_vertically(self, coordinate: List):
        pieces = set()
        for idx in range(0, self.size):
            if self.board.board[idx][coordinate[1]] is None: return False
            pieces.add(self.board.board[idx][coordinate[1]])
        return True if len(pieces) == 1 else False

    def _check_horizontally(self, coordinate: List):
        pieces = set()
        for idx in range(0, self.size):
            if self.board.board[coordinate[0]][idx] is None: return False
            pieces.add(self.board.board[coordinate[0]][idx])
        return True if len(pieces) == 1 else False

    def _check_forward_diagonal(self):
        pieces = set()
        for idx in range(0, self.size):
            if self.board.board[idx][self.size - idx - 1] is None: return False
            pieces.add(self.board.board[idx][self.size - idx - 1])
        return True if len(pieces) == 1 else False

    def _check_backward_diagonal(self):
        pieces = set()
        for idx in range(0, self.size):
            if self.board.board[idx][idx] is None: return False
            pieces.add(self.board.board[idx][idx])
        return True if len(pieces) == 1 else False

    def _check_winner(self, coordinate: List):
        if self._check_backward_diagonal(): return True
        if self._check_horizontally(coordinate): return True
        if self._check_forward_diagonal(): return True
        if self._check_vertically(coordinate): return True
        return False

    def print_board(self):
        for idx in range(self.size):
            for ele in self.board.board[idx]:
                print(ele, end=' ')
            print()

    def start_game(self):
        queue = deque()
        queue.extend(self.players)
        turn = self.size * self.size
        while turn != 0:
            coordinate = list(map(int, input("please pass the coordinate for the board").split(',')))
            if not self._check_coordinate_structure(coordinate): continue
            if not self._check_board_cell(coordinate): continue
            if not self._check_board_boundary(coordinate): continue
            player = queue.popleft()
            queue.append(player)
            self.board.board[coordinate[0]][coordinate[1]] = player.pieces
            self.print_board()
            if self._check_winner(coordinate):
                print(f'Winner is {player.name}')
                break

            turn -= 1
