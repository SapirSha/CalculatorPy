from CreateEquationTree import create_equation_tree, print_tree
from Equation import Equation
from BinTree import BinTree
from Operand import Operand



def main():
    gotten_input = "-1!*31^-2"
    equation = Equation(gotten_input)
    print(equation)
    equation_tree = create_equation_tree(equation)
    print("WA|\t ", end = '')
    print_tree(equation_tree)
    print(" \t|OK")

if __name__ == "__main__":
    main()