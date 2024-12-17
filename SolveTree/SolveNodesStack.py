from BinTree import BinTree
from SolveTree.CalculationError import CalculationError
from SolveTree.ExpectedType import TREE_OPER, ExpectedType
from SolveTree.GetExpectedType import get_expected_type
from Stack import Stack


def solve_nodes_stack(stack : Stack):
    node = BinTree()
    while not stack.is_empty():
        node = stack.pop()
        expected_type = get_expected_type(node)
        if expected_type == ExpectedType.operand:
            raise CalculationError("Error accrued while solving the tree")
        else:
            node.set_info(expected_type(node))

    return node.get_info()
