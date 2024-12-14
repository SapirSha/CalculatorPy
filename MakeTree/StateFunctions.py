from BinTree import BinTree
from Equation import Equation
from Stack import Stack


def state_start(tree : BinTree, equ : Equation, prev_trees : Stack):
    from MakeTree.StartTree import start_tree
    return start_tree(tree, equ, prev_trees)

def state_operator_binary(tree : BinTree, equ : Equation, prev_trees : Stack):
    from MakeTree.OperatorBinaryTree import operator_binary_tree
    return operator_binary_tree(tree, equ, prev_trees)

def state_operator_unary_right(tree : BinTree, equ : Equation, prev_trees : Stack):
    from MakeTree.OperatorUnaryRight import operator_unary_right_tree
    return operator_unary_right_tree(tree, equ, prev_trees)

def state_operator_unary_left(tree : BinTree, equ : Equation, prev_trees : Stack):
    from MakeTree.OperatorUnaryLeftTree import operator_unary_left_tree
    return operator_unary_left_tree(tree, equ, prev_trees)

def state_operand(tree : BinTree, equ : Equation, prev_trees : Stack):
    from MakeTree.OperandTree import operand_tree
    return operand_tree(tree, equ, prev_trees)

def state_open_brackets(tree: BinTree, equ: Equation, prev_trees: Stack):
    from MakeTree.MakeTree import make_tree
    from MakeTree.InsertToTree import insert_to_tree_tree
    equ.prev()
    equ, temp_tree = make_tree(equ)
    insert_to_tree_tree(tree, temp_tree, prev_trees)
    state = state_after_brackets

def state_after_brackets(tree: BinTree, equ: Equation, prev_trees: Stack):
    from MakeTree.AfterBracketsTree import after_brackets_tree
    return after_brackets_tree(tree, equ, prev_trees)

#Not Used
def state_close_brackets(tree: BinTree, equ: Equation, prev_trees: Stack):
    equ.prev()


