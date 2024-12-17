from BinTree import BinTree
from SolveTree.SolveNodesStack import solve_nodes_stack
from SolveTree.TreeToStackOfNodes import get_trees_internal_nodes

# the function that handles the solving of the tree
def solve_tree(tree : BinTree):
    # make a stack of the internal nodes (operators)
    nodes = get_trees_internal_nodes(tree)

    # if stack empty no internal node, in other words, no operators
    if nodes.is_empty():
        return tree.get_info()

    # solves and return the stack
    return solve_nodes_stack(nodes)