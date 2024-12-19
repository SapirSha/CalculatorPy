from BinTree import BinTree
from Equation import Equation
from MakeTree.InsertToTree import insert_to_tree_operator_unary_right, insert_to_tree_operator_binary
from MakeTree.IsOperatorTypes import is_cur_operator_unary_r_in_equation, get_operator, is_operator_binary, \
    is_operator_unary_l
from MakeTree.States import States
from Operand import is_operand
from Operators_Dictionary import CLOSE_PARENTHESES, OPEN_PARENTHESES
from Stack import Stack


# this function represent a state where the previous gotten input was Operand
def operand_tree(tree: BinTree, equ: Equation, prev_trees: Stack) -> (BinTree, Equation, Stack, int):
    equ.remove_white_space()

    if is_cur_operator_unary_r_in_equation(equ):
        tree, prev_trees = insert_to_tree_operator_unary_right(tree, get_operator(equ.curr()), prev_trees)
        return tree, equ, prev_trees, States.operator_unary_right
    elif is_operator_binary(equ.curr()):
        tree, prev_trees = insert_to_tree_operator_binary(tree, get_operator(equ.curr()), prev_trees)
        return tree, equ, prev_trees, States.operator_binary
    elif equ.curr() in CLOSE_PARENTHESES:
        return tree, equ, prev_trees, States.close_parentheses
    else:
        # Errors
        if is_operand(equ.curr()) and not equ.curr() == '.':
            equ.prev()
            raise SyntaxError("Spaces inside of an operand are not allowed")
        elif equ.curr() == '.':
            raise SyntaxError(
                "Syntax error: '.' can only be used inside an operand, and can only be used once per operand")
        elif equ.curr() in OPEN_PARENTHESES:
            raise SyntaxError("Open parentheses cannot come directly after operand")
        elif is_operator_unary_l(equ.curr()):
            raise SyntaxError("Operator unary left may not come After Operand")
        else:
            raise SyntaxError("Invalid Syntax: " + equ.curr())
