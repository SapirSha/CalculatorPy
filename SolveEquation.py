from BinTree import BinTree
from CountBrackets import count_brackets
from Equation import Equation
from MakeTree.MakeTree import make_tree
from SolveTree.CalculationError import CalculationError
from SolveTree.SolveTree import solve_tree

def print_tree(tree : BinTree):
    if tree is None:
        return
    print(tree.get_info(), end = ' ')
    print_tree(tree.get_left())
    print_tree(tree.get_right())


def solve_equation(equation : str):
    gotten_input = equation
    equ = Equation(gotten_input)

    print(equ)

    try:
        count_brackets(equ)
        equ, tree = make_tree(Equation(gotten_input))
        prefix = tree

        result = solve_tree(tree)

        print_tree(prefix)
        print()
        print(result)

    except SyntaxError as e:
        if e.msg is not None:
            print(equ.index * ' ' + '^')
            print(e)
    except OverflowError as e:
        print("Maybe lower the numbers? a little to big if i may say so")
    except CalculationError as e:
        print(e)