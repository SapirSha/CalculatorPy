from BinTree import BinTree
from CreateEquationTree import print_tree
from Equation import Equation
from MakeTree.InsertToTree import insert_to_tree_operator_unary_right, insert_to_tree_operator_binary
from MakeTree.States import States
from MakeTree.IsOperatorTypes import is_cur_operator_unary_r_in_equation, get_operator, is_operator_binary, \
    is_operator_unary_l
from Operand import is_operand
from Operators_Dictionary import CLOSE_BRACKETS, OPEN_BRACKETS
from Stack import Stack


def operator_unary_right_tree(tree : BinTree, equ : Equation, prev_trees : Stack ) -> (BinTree, Equation, Stack, int):
    equ.remove_white_space()

    if is_cur_operator_unary_r_in_equation(equ):
        tree, prev_trees = insert_to_tree_operator_unary_right(tree, get_operator(equ.curr()), prev_trees)
        return tree, equ, prev_trees, States.operator_unary_right
    elif is_operator_binary(equ.curr()):
        tree, prev_trees = insert_to_tree_operator_binary(tree, get_operator(equ.curr()), prev_trees)
        return tree, equ, prev_trees, States.operator_binary
    elif equ.curr() in CLOSE_BRACKETS:
        return tree, equ, prev_trees, States.close_brackets
    else:
        #Errors
        if is_operator_unary_l(equ.curr()):
            raise SyntaxError("Operator-unary-left cannot come after operator-unary-right")
        elif equ.curr() in OPEN_BRACKETS:
            raise SyntaxError("Missing operator-binary between operator-unary-right and Open brackets '(")
        elif is_operand(equ.curr()):
            raise SyntaxError("Operand cannot come right after operator-unary-right")
        else:
            raise SyntaxError("Invalid Syntax: " + equ.curr())