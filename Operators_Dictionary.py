from Operators.Ampersand import Ampersand
from Operators.AtSign import AtSign
from Operators.Dollar import Dollar
from Operators.Operator import Operator
from Operators.Asterisk import Asterisk
from Operators.Caret import Caret
from Operators.ExclamationMark import ExclamationMark
from Operators.Percent import Percent
from Operators.Slash import Slash
from Operators.Minus import Minus
from Operators.Plus import Plus
from Operators.Tilde import Tilde
from Operators.Hash import Hash

# this list holds all the operators instances that are active
OPERATORS = [
    Plus(),
    Minus(),
    Asterisk(),
    Slash(),
    Caret(),
    ExclamationMark(),
    Tilde(),
    Percent(),
    Dollar(),
    Ampersand(),
    AtSign(),
    Hash()
]

# this dictionary will hold the symbol of the operator as its key and the operator instance as its value
operators_dictionary = {}

OPEN_PARENTHESES = ['(']  # close brackets list
CLOSE_PARENTHESES = [')']  # open brackets list

# this dictionary would hold the brackets to know which open bracket is for which close parentheses {Open : Close}
DIC_PARENTHESES = {
    '(': ')',
}


# function to create the operators dictionary from the list: puts key as symbol and operator instance as key
def create_operators_dictionary():
    global operators_dictionary

    if operators_dictionary == {}:
        operators_dictionary = {}
        for operator in OPERATORS:
            operators_dictionary[operator.get_symbol()] = operator
    else:
        pass # dictionary already created

# retrieves the operator instance from the dictionary
def get_operator(symbol: str) -> Operator:
    return operators_dictionary.get(symbol)


# create dictionary at start
create_operators_dictionary()
