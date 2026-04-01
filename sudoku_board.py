from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        newLine = True
        for row in range(1, 10):
            for column in range(1, 10):
                if newLine == True:
                    newLine = False
                    s = s + f'{self.sudoku[row, column]}'
                else:
                    if ((column-1) % 3) == 0:
                        s = s + f'  {self.sudoku[row, column]}'
                    else:
                        s = s + f' {self.sudoku[row, column]}'
            if ((row % 3)) == 0:
                s = s + '\n\n'
            else:
                s = s + '\n'
            newLine = True
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
