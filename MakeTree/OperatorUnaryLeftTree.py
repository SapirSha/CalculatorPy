from BinTree import BinTree
from Equation import Equation
from MakeTree.InsertToTree import insert_to_tree_operator_unary_left, insert_to_tree_operand
from MakeTree.States import States
from MakeTree.UtilsOperandTree import get_operand_from_equ
from Operand import is_operand, Operand
from MakeTree.IsOperatorTypes import is_operator_unary_l, get_operator, is_cur_operator_unary_r_in_equation, \
    is_operator_binary
from Operators_Dictionary import OPEN_BRACKETS, CLOSE_BRACKETS
from Stack import Stack

# this function represent a state where the previous gotten input was unary-left operator
def operator_unary_left_tree(tree : BinTree, equ : Equation, prev_trees : Stack) -> (BinTree, Equation, Stack, int):
    equ.remove_white_space()

    if is_operand(equ.curr()):
        equ, oper = get_operand_from_equ(equ)
        insert_to_tree_operand(tree,oper,prev_trees)
        return tree, equ, prev_trees, States.operand
    elif is_operator_unary_l(equ.curr()):
        tree, prev_trees = insert_to_tree_operator_unary_left(tree, get_operator(equ.curr()), prev_trees)
        return tree, equ, prev_trees, States.operator_unary_left
    elif equ.curr() in OPEN_BRACKETS:
        return tree, equ, prev_trees, States.open_brackets
    else:
        #Errors
        if is_cur_operator_unary_r_in_equation(equ):
            raise SyntaxError("Operator-unary-right cannot come After operator-unary-left")
        elif is_operator_binary(equ.curr()):
            raise SyntaxError("Operator-binary cannot come after operator-unary-left")
        elif equ.curr() in CLOSE_BRACKETS:
            raise SyntaxError("Missing Operand after operator-unary-left")
        else:
            raise SyntaxError("Invalid Syntax: " + equ.curr())
