from enum import Enum


TREE_PRIO = 1
TREE_OPER = 0

class ExpectedType(Enum):
    operand = 0
    operator_binary = 1
    operator_unary_left = 2
    operator_unary_right = 3