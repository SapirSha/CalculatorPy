from CountParentheses import count_parentheses
from Equation import Equation
from MakeTree.MakeTree import make_tree
from SolveTree.CalculationError import CalculationError
from SolveTree.SolveTree import solve_tree


# the main function the calls to solve the equation
def solve_equation(equation: str):
    gotten_input = equation
    equ = Equation(gotten_input)

    try:
        # first checks if the brackets are correctly placed
        count_parentheses(equ)
        # then creates the appropriate tree for the equation
        equ, tree = make_tree(Equation(gotten_input))
        # then solves the tree
        result = solve_tree(tree)

        # and finally returns the result
        return result.get_data()

    # can happen when syntax problem accrues
    except SyntaxError as e:
        if e.msg is not None:
            print("<--- Error ------------------------------>")
            print(equ)
            print(equ.index * ' ' + '^')
            print(e)
            print("<---------------------------------------->")
        raise
    # can happen when equation numbers are too big
    except OverflowError as e:
        print("<--- Error ------------------------------>")
        print("Numbers too big: reached Overflow")
        print("<---------------------------------------->")
        raise
    # can happen when an operator gets an invalid number
    except CalculationError as e:
        print("<--- Error ------------------------------>")
        print(e.message)
        print("<---------------------------------------->")
        raise
    # unknown exception case
    except Exception as e:
        print("<--- Error ------------------------------>")
        print("UNKNOWN EXCEPTION ACCRUED")
        print(e)
        print("<---------------------------------------->")
        raise
