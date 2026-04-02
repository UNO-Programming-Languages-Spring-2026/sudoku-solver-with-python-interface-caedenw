from typing import Tuple
import clingo
import sys
from sudoku_board import Sudoku

class Context:
    def __init__(self, board: Sudoku):
        self.board = board.sudoku
    
    def initial(self) -> list[clingo.symbol.Symbol]:
        returnList = []
        for key in self.board.keys():
            x = clingo.Number(key[0])
            y = clingo.Number(key[1])
            z = clingo.Number(self.board[key])
            returnList.append(clingo.Tuple_((x, y, z)))
        return returnList

class SudokuSolver(clingo.application.Application):
    def main(self, control, files):
        for file in files:
            fileHandle = open(file, 'r')
            context = Context(Sudoku({}).from_str(fileHandle.read()))
            fileHandle.close()
        if len(files) > 0:
            control.load('sudoku.lp')
            control.load('sudoku_py.lp')
            control.ground(context=context)
            control.solve()
    
    def print_model(self, model, printer):
        print(str(Sudoku({}).from_model(model)))
        sys.stdout.flush()

clingo.application.clingo_main(SudokuSolver())