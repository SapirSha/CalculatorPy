from enum import Enum

TREE_PRIO = 1
TREE_OPER = 0


class ExpectedType(Enum):
    from SolveTree.ExpectedOperatorFunction import expected_operand, expected_operator_binary, \
        expected_operator_unary_left, expected_operator_unary_right
    operand = expected_operand
    operator_binary = expected_operator_binary
    operator_unary_left = expected_operator_unary_left
    operator_unary_right = expected_operator_unary_right
