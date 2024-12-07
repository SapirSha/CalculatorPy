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


create_operators_dictionary()
