from BinTree import BinTree
from SolveTree.ExpectedType import ExpectedType

# gets expected type according to the children in the tree
def get_expected_type(tree : BinTree):
    # since no children -> expected operand
    if tree.get_right() is None and tree.get_left() is None:
        return ExpectedType.operand
    # since two children -> expected operator binary
    elif tree.get_left() is not None and tree.get_right() is not None:
        return ExpectedType.operator_binary
    # since only right child (somthing to the right of operator) -> operator unary left
    elif tree.get_right() is not None:
        return ExpectedType.operator_unary_left
    # since only left child (somthing to the left of operator) -> operator unary right
    elif tree.get_left() is not None:
        return ExpectedType.operator_unary_right