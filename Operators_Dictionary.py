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
from Operators.Tilde import Tilde
from Operators.UnaryLOperator import UnaryLOperator
from Operators.UnaryROperator import UnaryROperator

OPERATORS = [
    Plus(),
    Minus(),
    Asterisk(),
    Slash(),
    Caret(),
    ExclamationMark(),
    Tilde()
]

operators_dictionary = {}


def create_operators_dictionary():
    global operators_dictionary

    if operators_dictionary == {}:
        operators_dictionary = {}
        for operator in OPERATORS:
            operators_dictionary[operator.get_symbol()] = operator
    else:
        pass


def get_operator(symbol: str) -> Operator:
    return operators_dictionary.get(symbol)


create_operators_dictionary()
