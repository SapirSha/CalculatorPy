from BinTree import BinTree
from SolveTree.CalculationError import CalculationError
from SolveTree.ExpectedType import ExpectedType
from SolveTree.GetExpectedType import get_expected_type
from Stack import Stack


def solve_nodes_stack(stack : Stack):
    node = BinTree()

    while not stack.is_empty():
        node = stack.pop()
        # the expected operator type (binary/unary-right/unary-left)
        expected_type = get_expected_type(node)
        # stack should only have the operators
        if expected_type == ExpectedType.operand:
            raise CalculationError("Error accrued while solving the tree")
        else:
            # expected type is an enum that holds the function depending on the expected operator
            node.set_info(expected_type(node))

    return node.get_info()
