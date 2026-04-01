from typing import Tuple
import clingo
import sys

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
        symbols = sorted(model.symbols(shown=True))
        symbolsStr = ''
        for symbol in symbols:
            if (len(symbolsStr) != 0):
                symbolsStr = f'{symbolsStr} {str(symbol)}'
            else:
                symbolsStr = str(symbol)
        print(symbolsStr)
        sys.stdout.flush()

clingo.application.clingo_main(SudokuSolver())