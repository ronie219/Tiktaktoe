from Board import Board
from Game import Game
from Player import Player
from Symbols import Symbols

if __name__ == '__main__':
    board = Board(3)
    player1 = Player('Abhishek',Symbols.X.value)
    player2 = Player('Ronnie', Symbols.O.value)
    game = Game(players=[player1, player2], board=board, size=3)
    game.start_game()