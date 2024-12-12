from BinTree import BinTree
from Equation import Equation
from MakeTree.InsertToTree import insert_to_tree_operator_unary_left
from MakeTree.States import States
from Operand import is_operand, Operand
from Operators_Dictionary import is_operator_unary_l, get_operator
from Stack import Stack


def operator_binary_tree(tree : BinTree, equ : Equation, prev_trees : Stack) -> (BinTree, Equation, Stack, int):
    equ.remove_white_space()

    if is_operand(equ.curr()):
        tree.set_right(Operand(int(equ.curr())))
        return tree, equ, prev_trees, States.operand
    elif is_operator_unary_l(equ.curr()):
        insert_to_tree_operator_unary_left(tree, get_operator(equ.curr()), prev_trees)
        return tree, equ, prev_trees, States.operator_unary_left
    elif equ.curr() == '(':
        pass
    else:
        raise SyntaxError(" after binary operator has to be ( \ operand \ operator left")