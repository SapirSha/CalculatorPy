from enum import Enum


TREE_PRIO = 1
TREE_OPER = 0

class States(Enum):
    start = 0
    operator_unary_left = 1
    operand = 2
    operator_unary_right = 3
    operator_binary = 4
    open_brackets = 5
    close_brackets = 6