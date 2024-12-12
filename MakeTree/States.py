from enum import Enum

class States(Enum):
    start = 0
    operator_unary_left = 1
    operand = 2
    operator_unary_right = 3
    whitespace = 4
    operator_binary = 5