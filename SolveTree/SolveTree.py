from BinTree import BinTree
from SolveTree.GetExpectedType import get_expected_type

# the function that handles the solving of the tree
def solve_tree(tree : BinTree):
    # calls the appropriate function for the type that the current node is supposed to be (depends on the children of the node)
    return get_expected_type(tree)(tree)