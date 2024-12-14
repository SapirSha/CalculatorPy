from BinTree import BinTree
from SolveTree.GetExpectedType import get_expected_type

def solve_tree(tree : BinTree):
    expected_type = get_expected_type(tree)
    return expected_type(tree)