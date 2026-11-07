from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    def __str__(self) -> str:
        s = ""
        for row in range(1, 10):
            for col in range(1, 10):
                s += str(self.sudoku.get((row, col), "-"))

                if col < 9:
                    s += "  " if col % 3 == 0 else " "

            s += "\n"

            if row in (3, 6):
                s += "\n"
        return s

    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        cells = s.split()

        for index, cell in enumerate(cells):
            if cell != "-":
                row = index // 9 + 1
                col = index % 9 + 1
                sudoku[(row, col)] = int(cell)
        return cls(sudoku)

    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}
        for atom in model.symbols(shown=True):
            if atom.match("sudoku", 3):
                row = atom.arguments[0].number
                col = atom.arguments[1].number
                value = atom.arguments[2].number
                sudoku[(row, col)] = value
        return cls(sudoku)
