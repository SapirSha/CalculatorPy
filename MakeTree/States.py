from enum import Enum


TREE_PRIO = 1
TREE_OPER = 0

class States(Enum):
    start = 0
    operator_unary_left = 1
    operand = 2
    operator_unary_right = 3
    whitespace = 4
    operator_binary = 5