from CreateEquationTree import create_equation_tree
from Equation import Equation
from BinTree import BinTree
from MakeTree.MakeTree import make_tree
from MakeTree.UtilsOperandTree import get_operand_from_equ
from Operand import Operand
from MakeTree.IsOperatorTypes import is_cur_operator_unary_r_in_equation

def print_tree(tree : BinTree):
    if tree is None:
        return
    print(tree.get_info(), end = ' ')
    print_tree(tree.get_left())
    print_tree(tree.get_right())

def main():

    gotten_input = "5 +(5)%2"
    equ = Equation(gotten_input)

    print(equ)
    equ, tree = make_tree(Equation(gotten_input))

    print_tree(tree)


if __name__ == "__main__":
    main()