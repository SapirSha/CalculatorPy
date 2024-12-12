from CreateEquationTree import create_equation_tree, print_tree
from Equation import Equation
from BinTree import BinTree
from MakeTree.MakeTree import make_tree
from Operand import Operand
from Operators_Dictionary import is_cur_operator_unary_r_in_equation


def main():
    gotten_input = "552 - 572 ! 4"
    equ = Equation(gotten_input)


    make_tree(Equation(gotten_input))

if __name__ == "__main__":
    main()