from enum import Enum

from MakeTree.StateFunctions import state_start, state_operator_unary_left, state_operand, state_operator_unary_right, \
    state_operator_binary, state_open_parentheses, state_close_parentheses, state_after_parentheses

# tree holds both Priority and the operator, that it the same operator may have multiple priority's, such as in minus unary and minus binary
TREE_PRIO = 1
TREE_OPER = 0


# enum that holds the functions for each state
class States(Enum):
    start = state_start
    operator_unary_left = state_operator_unary_left
    operand = state_operand
    operator_unary_right = state_operator_unary_right
    operator_binary = state_operator_binary
    open_brackets = state_open_parentheses
    close_parentheses = state_close_parentheses
    after_parentheses = state_after_parentheses
