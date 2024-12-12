from BinTree import BinTree
from Equation import Equation
from Operand import is_operand
from Operators.BinaryOperator import BinaryOperator
from Operators.Operator import Operator

from Operators.Asterisk import Asterisk
from Operators.Caret import Caret
from Operators.ExclamationMark import ExclamationMark
from Operators.Slash import Slash
from Operators.Minus import Minus
from Operators.Plus import Plus
from Operators.UnaryLOperator import UnaryLOperator
from Operators.UnaryROperator import UnaryROperator

OPERATORS = [
    Plus(),
    Minus(),
    Asterisk(),
    Slash(),
    Caret(),
    ExclamationMark()
]

operators_dictionary = {}


def create_operators_dictionary():
    global operators_dictionary

    if operators_dictionary == {}:
        print("Creating Dictionary! ")
        operators_dictionary = {}
        for operator in OPERATORS:
            operators_dictionary[operator.get_symbol()] = operator
    else:
        print("Dictionary already created")


def get_operator(symbol: str) -> Operator:
    return operators_dictionary.get(symbol)

def is_operator(symbol: str) -> bool:
    return get_operator(symbol) is not None


def is_operator_binary(symbol: str) -> bool:
    return is_operator(symbol) and isinstance(get_operator(symbol), BinaryOperator)


def is_operator_unary_l(symbol: str) -> bool:
    return is_operator(symbol) and isinstance(get_operator(symbol), UnaryLOperator)


def is_operator_unary_r(symbol: str) -> bool:
    return is_operator(symbol) and isinstance(get_operator(symbol), UnaryROperator)

def is_cur_operator_unary_r_in_equation(equ : Equation) -> bool:
    current = equ.curr()

    if not is_operator_unary_r(current):
        return False
    elif not is_operator_binary(current):
        return True
    try:
        next_symb = equ.next_non_space()
    except StopIteration:
        return True
    if is_operand(next_symb):
        return False
    elif next_symb == '(':
        return False
    elif next_symb == ')':
        return True
    elif not is_operator(next_symb):
        raise SyntaxError("Invalid Symbol: " + next_symb)

    # compare with the next operator
    operc = get_operator(current)
    opern = get_operator(next_symb)
    if isinstance(opern, UnaryROperator) and not isinstance(opern, BinaryOperator) and not isinstance(opern, UnaryLOperator):
        return True
    elif not isinstance(opern, UnaryROperator) and  isinstance(opern, BinaryOperator) and not isinstance(opern, UnaryLOperator):
        return True
    if not isinstance(opern, UnaryROperator) and not isinstance(opern, BinaryOperator) and isinstance(opern, UnaryLOperator):
        return False
    if isinstance(opern, UnaryROperator) and isinstance(opern, BinaryOperator) and not isinstance(opern, UnaryLOperator):
        return True
    if isinstance(opern, UnaryROperator) and not isinstance(opern, BinaryOperator) and isinstance(opern, UnaryLOperator):
        pass # -------------------------------------------------------------
    if not isinstance(opern, UnaryROperator) and  isinstance(opern, BinaryOperator) and isinstance(opern, UnaryLOperator):
        if opern.get_unary_l_priority() > operc.get_unary_r_priority():
            return False
        return True
    if  isinstance(opern, UnaryROperator) and  isinstance(opern, BinaryOperator) and isinstance(opern, UnaryLOperator):
        priol, priob, prior = opern.get_unary_l_priority(), opern.get_binary_priority(), opern.get_unary_r_priority()
        if max(operc.get_unary_r_priority(), priol, priob,prior) == operc.get_unary_r_priority():
            return True
        elif max(operc.get_unary_r_priority(), priol, priob,prior) == priol:
            pass # ----------------------------------------------------------------
        else:
            return True


def expected_binary(tree: BinTree):
    return tree.get_left() is not None and tree.get_right() is not None

def expected_unary_r(tree: BinTree):
    return tree.get_left() is not None and tree.get_right() is None

def expected_unary_l(tree: BinTree):
    return tree.get_left() is None and tree.get_right() is not None


create_operators_dictionary()