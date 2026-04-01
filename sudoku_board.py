from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        # YOUR CODE HERE
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        symbols = sorted(model.symbols(shown=True))
        for symbol in symbols:
            symbolList = str(symbol).split(',')
            x = int(symbolList[0][len(symbolList[0])-1])
            y = int(symbolList[1])
            z = int(symbolList[2][0])
            sudoku[(x, y)] = z
        return cls(sudoku)
