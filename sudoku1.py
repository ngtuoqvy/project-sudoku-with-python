import clingo


class ClingoApp(clingo.application.Application):

    def main(self, ctl, files):
        ctl.load("sudoku.lp")

        for f in files:
            ctl.load(f)

        if not files:
            ctl.load("-")

        ctl.ground()
        ctl.solve()

    def print_model(self, model, printer):
        atoms = sorted(str(atom) for atom in model.symbols(shown=True))
        print(" ".join(atoms))


if __name__ == "__main__":
    clingo.application.clingo_main(ClingoApp())