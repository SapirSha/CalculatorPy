from BinTree import BinTree
from CreateEquationTree import print_tree
from Equation import Equation
from MakeTree.States import TREE_PRIO, TREE_OPER
from Operand import Operand
from Operators.Minus import Minus
from Operators.Operator import Operator
from Operators.Tilde import Tilde
from Operators.UnaryROperator import UnaryROperator
from Operators_Dictionary import get_operator
from Stack import Stack


def insert_to_tree_operator_unary_right(tree : BinTree, oper : Operator, prev_trees: Stack) -> (BinTree, Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_unary_r_priority()))
    elif isinstance(tree.get_info(), Operand):
        tree = BinTree((oper, oper.get_unary_r_priority()), tree)
        return tree, prev_trees
    else:
        while tree.get_info()[TREE_PRIO] >= oper.get_unary_r_priority() and not prev_trees.is_empty():
            tree = prev_trees.pop()

        if tree.get_info()[TREE_PRIO] >= oper.get_unary_r_priority():
            tree = BinTree((oper, oper.get_unary_r_priority()), tree)
        else:
            tree.set_right((oper, oper.get_unary_r_priority()), tree.get_right())
            prev_trees.push(tree)
            tree = tree.get_right()

    return tree, prev_trees

def insert_to_tree_operator_binary(tree : BinTree, oper : Operator, prev_trees : Stack) -> (BinTree, Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_binary_priority()))
    elif isinstance(tree.get_info(), Operand):
        tree = BinTree((oper, oper.get_binary_priority()), tree)
        return tree, prev_trees
    else:
        while tree.get_info()[TREE_PRIO] >= oper.get_binary_priority() and not prev_trees.is_empty():
            tree = prev_trees.pop()

        if tree.get_info()[TREE_PRIO] >= oper.get_binary_priority():
            tree = BinTree((oper, oper.get_binary_priority()), tree)
        else:
            if isinstance(tree.get_info()[TREE_OPER], UnaryROperator):
                if prev_trees.is_empty():
                    tree = BinTree((oper, oper.get_binary_priority()), tree)
                    return tree, prev_trees
                else:
                    tree = prev_trees.pop()
            tree.set_right((oper, oper.get_binary_priority()), tree.get_right())
            prev_trees.push(tree)
            tree = tree.get_right()

    return tree, prev_trees

def insert_to_tree_operator_unary_left(tree : BinTree, oper : Operator, prev_trees : Stack) -> (BinTree, Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_unary_l_priority()))
    elif isinstance(tree.get_info(), Operand):
            tree = BinTree((oper, oper.get_unary_l_priority()), tree)
            return tree, prev_trees
    else:
        # needs to come before the binary no matter the priority
        if isinstance(tree.get_info()[TREE_OPER], Tilde) and not isinstance(oper, Minus):
            raise SyntaxError("Operator Tilde(~) must come before a number, unary minus or (, instead got: " + oper.get_symbol())
        elif isinstance(oper, Minus) and not (isinstance(tree.get_info()[TREE_OPER], Minus) and tree.get_info()[TREE_PRIO] == get_operator('-').get_unary_l_priority()):
            tree.set_right((oper, "Assigned Minus"), None, tree.get_right())
        elif isinstance(tree.get_info()[TREE_OPER], Minus) and tree.get_info()[TREE_PRIO] == get_operator('-').get_unary_l_priority() and not isinstance(oper, Minus):
            raise SyntaxError("Operator Unary Minus must come before a number, another minus or (, instead got: " + oper.get_symbol())
        else:
            if tree.get_right() is None or not isinstance(tree.get_right().get_info()[TREE_OPER], Minus):
                tree.set_right((oper, oper.get_unary_l_priority()), tree.get_right())
                prev_trees.push(tree)
                tree = tree.get_right()

    return tree, prev_trees

def insert_to_tree_operand(tree : BinTree, oper : Operand, prev_trees : Stack) -> None:
    while tree.get_right() is not None and not isinstance(tree.get_right().get_info(), Operand):
        tree = tree.get_right()
    if tree.get_right() is None:
        tree.set_right(oper)
    else:
        tree.set_right(tree.get_right().get_info() * 10 + oper.get_data())

def insert_to_tree_tree(tree : BinTree, ttree : BinTree, prev_trees : Stack) -> None:
    while tree.get_right() is not None:
        tree = tree.get_right()
    tree.set_right_tree(ttree)