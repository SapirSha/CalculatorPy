from BinTree import BinTree
from Equation import Equation
from MakeTree.States import States
from Operand import is_operand, Operand
from Operators_Dictionary import is_operator_unary_l, get_operator
from Stack import Stack


def operator_unary_left_tree(tree : BinTree, equ : Equation, prev_trees : Stack) -> (BinTree, Equation, Stack, int):
    equ.remove_white_space()

    if is_operand(equ.curr()):
        tree.set_right(Operand(int(equ.curr())))
        return tree, equ, prev_trees, States.operand
    elif is_operator_unary_l(equ.curr()):
        tree.set_right((get_operator(equ.curr()), get_operator(equ.curr()).get_unary_l_priority()), tree.get_left(), tree.get_right())
        prev_trees.push(tree)
        tree = tree.get_right()
        return tree, equ, prev_trees, States.operator_unary_left
    elif equ.curr() == '(':
        pass
    else:
        raise SyntaxError("after unary left operator should come operand or ( or operator unary left, instead got: " + equ.curr())
