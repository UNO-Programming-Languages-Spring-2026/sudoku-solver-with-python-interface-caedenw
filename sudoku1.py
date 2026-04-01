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
        # YOUR CODE HERE
        return cls(sudoku)

clingo.application.clingo_main(SudokuSolver())