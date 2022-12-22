from Symbols import Symbols


class Pieces:

    def __init__(self, symbol: Symbols) -> None:
        self.symbol = symbol

    def __str__(self):
        return f'{self.symbol}'
