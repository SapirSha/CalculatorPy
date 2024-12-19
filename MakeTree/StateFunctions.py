from BinTree import BinTree
from Equation import Equation
from Stack import Stack


# utility for start state in case want to add somthing
def state_start(tree: BinTree, equ: Equation, prev_trees: Stack):
    from MakeTree.StartTree import start_tree
    return start_tree(tree, equ, prev_trees)


# utility for operator binary state in case want to add somthing
def state_operator_binary(tree: BinTree, equ: Equation, prev_trees: Stack):
    from MakeTree.OperatorBinaryTree import operator_binary_tree
    return operator_binary_tree(tree, equ, prev_trees)


# utility for operator unary right state in case want to add somthing
def state_operator_unary_right(tree: BinTree, equ: Equation, prev_trees: Stack):
    from MakeTree.OperatorUnaryRight import operator_unary_right_tree
    return operator_unary_right_tree(tree, equ, prev_trees)


# utility for operator unary left state in case want to add somthing
def state_operator_unary_left(tree: BinTree, equ: Equation, prev_trees: Stack):
    from MakeTree.OperatorUnaryLeftTree import operator_unary_left_tree
    return operator_unary_left_tree(tree, equ, prev_trees)


# utility for operand state in case want to add somthing
def state_operand(tree: BinTree, equ: Equation, prev_trees: Stack):
    from MakeTree.OperandTree import operand_tree
    return operand_tree(tree, equ, prev_trees)


# utility for Open brackets state in case want to add somthing
# this function mostly makes a new tree and puts it in the appropriate place
def state_open_parentheses(tree: BinTree, equ: Equation, prev_trees: Stack):
    from MakeTree.MakeTree import make_tree
    from MakeTree.InsertToTree import insert_to_tree_tree
    equ.prev()
    equ, temp_tree = make_tree(equ)
    insert_to_tree_tree(tree, temp_tree, prev_trees)
    state = state_after_parentheses
    return tree, equ, prev_trees, state


# utility for after brackets state in case want to add somthing
def state_after_parentheses(tree: BinTree, equ: Equation, prev_trees: Stack):
    from MakeTree.AfterParenthesesTree import after_parentheses_tree
    return after_parentheses_tree(tree, equ, prev_trees)


# utility for close brackets state in case want to add somthing
# this function is pretty much designed to break the loop in the 'maketree' function
def state_close_parentheses(tree: BinTree, equ: Equation, prev_trees: Stack):
    equ.prev()
    raise StopIteration
