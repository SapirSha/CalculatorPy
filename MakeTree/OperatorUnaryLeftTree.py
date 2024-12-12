from BinTree import BinTree
from Equation import Equation
from MakeTree.InsertToTree import insert_to_tree_operator_unary_left, insert_to_tree_operand
from MakeTree.States import States
from Operand import is_operand, Operand
from Operators_Dictionary import is_operator_unary_l, get_operator
from Stack import Stack


def operator_unary_left_tree(tree : BinTree, equ : Equation, prev_trees : Stack) -> (BinTree, Equation, Stack, int):
    equ.remove_white_space()

    if is_operand(equ.curr()):
        temp = 0
        try:
            while is_operand(equ.curr()):
                temp = temp * 10 + int(equ.curr())
                next(equ)
            equ.prev()
        finally:
            insert_to_tree_operand(tree,Operand(temp),prev_trees)
        return tree, equ, prev_trees, States.operand
    elif is_operator_unary_l(equ.curr()):
        tree, prev_trees = insert_to_tree_operator_unary_left(tree, get_operator(equ.curr()), prev_trees)
        return tree, equ, prev_trees, States.operator_unary_left
    elif equ.curr() == '(':
        return tree, equ, prev_trees, States.open_brackets
    else:
        raise SyntaxError("after unary left operator should come operand or ( or operator unary left, instead got: " + equ.curr())
