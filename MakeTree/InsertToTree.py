from BinTree import BinTree
from Equation import Equation
from Operators.Operator import Operator
from Stack import Stack


def insert_to_tree_operator_unary_right(tree : BinTree, oper : Operator, prev_trees: Stack) -> (BinTree, Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_unary_r_priority()))
    else:
        pass

    return tree, oper

def insert_to_tree_operator_binary(tree : BinTree, oper : Operator, prev_trees : Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_binary_priority()))
    else:
        pass

    return tree, oper

def insert_to_tree_operator_unary_left(tree : BinTree, oper : Operator, prev_trees : Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_unary_l_priority()))
    else:
        pass

    return tree, oper