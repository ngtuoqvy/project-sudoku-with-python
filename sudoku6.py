import sys
import clingo
from sudoku_board import Sudoku


class Context:
    def __init__(self, board: Sudoku):
        self.board = board

    def initial(self) -> list[clingo.symbol.Symbol]:
        symbols = []

        for (row, col), value in sorted(self.board.sudoku.items()):
            symbols.append(
                clingo.Function(
                    "",
                    [
                        clingo.Number(row),
                        clingo.Number(col),
                        clingo.Number(value),
                    ],
                    True,
                )
            )

        return symbols


class ClingoApp(clingo.application.Application):
    def main(self, ctl, files):
        if files:
            with open(files[0], encoding="utf-8") as f:
                text = f.read()
        else:
            text = sys.stdin.read()

        board = Sudoku.from_str(text)
        context = Context(board)

        ctl.load("sudoku.lp")
        ctl.load("sudoku_py.lp")
        ctl.ground([("base", [])], context=context)
        ctl.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku, end="")


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())