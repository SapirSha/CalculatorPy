from BinTree import BinTree
from CreateEquationTree import print_tree
from Equation import Equation
from MakeTree.States import TREE_PRIO
from Operators.Operator import Operator
from Operators_Dictionary import get_operator
from Stack import Stack


def insert_to_tree_operator_unary_right(tree : BinTree, oper : Operator, prev_trees: Stack) -> (BinTree, Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_unary_r_priority()))
    else:
        while tree.get_info()[TREE_PRIO] >= oper.get_unary_r_priority() and not prev_trees.is_empty():
            tree = prev_trees.pop()

        if tree.get_info()[TREE_PRIO] >= oper.get_unary_r_priority():
            tree = BinTree((oper, oper.get_unary_r_priority()), tree)
        else:
            tree.set_right((oper, oper.get_unary_r_priority()), tree.get_left(),tree.get_right())
            prev_trees.push(tree)
            tree = tree.get_right()

    return tree, prev_trees

def insert_to_tree_operator_binary(tree : BinTree, oper : Operator, prev_trees : Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_binary_priority()))
    else:
        while tree.get_info()[TREE_PRIO] >= oper.get_binary_priority() and not prev_trees.is_empty():
            tree = prev_trees.pop()
        if tree.get_info()[TREE_PRIO] >= oper.get_binary_priority():
            tree = BinTree((oper, oper.get_binary_priority()), tree)

        else:
            tree.set_right((oper, oper.get_binary_priority()), tree.get_left(), tree.get_right())
            prev_trees.push(tree)
            tree = tree.get_right()

    return tree, prev_trees

def insert_to_tree_operator_unary_left(tree : BinTree, oper : Operator, prev_trees : Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_unary_l_priority()))
    else:
        pass

    return tree, prev_trees