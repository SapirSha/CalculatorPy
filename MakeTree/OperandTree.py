from BinTree import BinTree
from CreateEquationTree import print_tree
from Equation import Equation
from MakeTree.InsertToTree import insert_to_tree_operator_unary_right, insert_to_tree_operator_binary
from MakeTree.States import States
from Operand import is_operand
from Operators_Dictionary import is_cur_operator_unary_r_in_equation, get_operator, is_operator_binary
from Stack import Stack


def operand_tree(tree : BinTree, equ : Equation, prev_trees : Stack) -> (BinTree, Equation, Stack, int):

    if is_operand(equ.curr()):
        tree.set_right(tree.get_right().get_info() * 10 + int(equ.curr()))
        return tree, equ, prev_trees, States.operand
    elif equ.curr() == '.':
        pass
    else:
        equ.remove_white_space()
        if is_operand(equ.curr()):
            raise SyntaxError("Spaces between operands are not allowed")
        elif is_cur_operator_unary_r_in_equation(equ):
            tree, prev_trees = insert_to_tree_operator_unary_right(tree, get_operator(equ.curr()), prev_trees)
            return tree, equ, prev_trees, States.operator_unary_right
        elif is_operator_binary(equ.curr()):
            tree, prev_trees = insert_to_tree_operator_binary(tree, get_operator(equ.curr()), prev_trees)
            return tree, equ, prev_trees, States.operator_binary
        elif equ.curr() == ')':
            pass
        else:
            raise SyntaxError("after operand may only come right unary operator \ operator \ )")




