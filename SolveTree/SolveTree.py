from BinTree import BinTree
from MakeTree.States import TREE_OPER
from Operators.Caret import Caret
from SolveTree.GetExpectedType import get_expected_type
from SolveTree.SolveNodesStack import solve_nodes_stack
from SolveTree.TreeToStackOfNodes import get_trees_internal_nodes
from Stack import Stack

def p_stack(s : Stack):
    p = Stack()
    while not s.is_empty():
        if s.peek().get_left() is not None:
            print(s.peek().get_left().get_info(), end = " ")
        print(s.peek().get_info(), end = " ")
        if s.peek().get_right() is not None:
            print(s.peek().get_right().get_info(), end = "\t\t")

        p.push(s.pop())
    while not p.is_empty():
        #print(p.peek().get_info(), end = " ")
        s.push(p.pop())
    print()


# the function that handles the solving of the tree
def solve_tree(tree : BinTree):
    nodes = get_trees_internal_nodes(tree)

    p_stack(nodes)


    if nodes.is_empty():
        return tree.get_info()

    return solve_nodes_stack(nodes)





    # calls the appropriate function for the type that the current node is supposed to be (depends on the children of the node)
    #return get_expected_type(tree)(tree)
    raise Exception("GOOD")