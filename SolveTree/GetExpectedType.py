from BinTree import BinTree
from Operand import Operand
from SolveTree.ExpectedType import ExpectedType


def get_expected_type(tree : BinTree):
    if tree.get_right() is None and tree.get_left() is None:
        return ExpectedType.operand
    elif tree.get_left() is not None and tree.get_right() is not None:
        return ExpectedType.operator_binary
    elif tree.get_right() is not None:
        return ExpectedType.operator_unary_left
    elif tree.get_left() is not None:
        return ExpectedType.operator_unary_right