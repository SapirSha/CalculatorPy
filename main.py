
from CreateEquationTree import create_equation_tree
from Equation import Equation
from BinTree import BinTree
from MakeTree.MakeTree import make_tree
from MakeTree.UtilsOperandTree import get_operand_from_equ
from Operand import Operand
from MakeTree.IsOperatorTypes import is_cur_operator_unary_r_in_equation
from SolveTree.CalculationError import CalculationError
from SolveTree.SolveTree import solve_tree


def print_tree(tree : BinTree):
    if tree is None:
        return
    print(tree.get_info(), end = ' ')
    print_tree(tree.get_left())
    print_tree(tree.get_right())

def main():
    gotten_input = "~--- 7!"
    equ = Equation(gotten_input)

    print(equ)
    try:
        equ, tree = make_tree(Equation(gotten_input))
        prefix = tree
        result = solve_tree(tree)

        print_tree(prefix)
        print()
        print(result)

    except SyntaxError as e:
        print(equ.index * ' ' + '^')
        print(e)
    except OverflowError as e:
        print("Maybe lower the numbers? a little to big if i may say so")
    except CalculationError as e:
        print(e)



if __name__ == "__main__":
    main()