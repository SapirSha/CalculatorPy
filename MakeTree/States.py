from enum import Enum

from MakeTree.StateFunctions import state_start, state_operator_unary_left, state_operand, state_operator_unary_right, \
    state_operator_binary, state_open_brackets, state_close_brackets, state_after_brackets

TREE_PRIO = 1
TREE_OPER = 0

class States(Enum):
    start = state_start
    operator_unary_left = state_operator_unary_left
    operand = state_operand
    operator_unary_right = state_operator_unary_right
    operator_binary = state_operator_binary
    open_brackets = state_open_brackets
    close_brackets = state_close_brackets
    after_brackets = state_after_brackets
