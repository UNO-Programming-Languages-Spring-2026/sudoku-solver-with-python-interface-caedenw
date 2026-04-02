from typing import Tuple
import clingo
import sys
from sudoku_board import Sudoku

class SudokuSolver(clingo.application.Application):
    def main(self, control, files):
        for file in files:
            control.load('sudoku.lp')
            control.load(file)
        if len(files) == 0:
            control.load('sudoku.lp')
            control.load('-')
        control.ground()
        control.solve()
    
    def print_model(self, model, printer):
        print(str(Sudoku({}).from_model(model)))
        sys.stdout.flush()

clingo.application.clingo_main(SudokuSolver())