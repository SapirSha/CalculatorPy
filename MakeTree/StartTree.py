from BinTree import BinTree
from Equation import Equation
from MakeTree.InsertToTree import insert_to_tree_operator_unary_right, insert_to_tree_operator_binary, \
    insert_to_tree_operator_unary_left, insert_to_tree_operand
from MakeTree.MakeTree import make_tree
from MakeTree.States import States
from MakeTree.UtilsOperandTree import get_operand_from_equ
from Operand import is_operand, Operand
from MakeTree.IsOperatorTypes import is_operator_unary_l, is_operator, is_cur_operator_unary_r_in_equation, \
    get_operator, \
    is_operator_binary
from Operators_Dictionary import OPEN_PARENTHESES, CLOSE_PARENTHESES
from Stack import Stack


# this function represent the start phase to start a tree
def start_tree(tree: BinTree, equ: Equation, prev_trees: Stack):
    equ.remove_white_space()

    if is_operand(equ.curr()):
        equ, oper = get_operand_from_equ(equ)
        tree.set_info(oper) # the only time to insert an operand in the middle
        return tree, equ, prev_trees, States.operand

    elif is_operator_unary_l(equ.curr()):
        tree, prev_trees = insert_to_tree_operator_unary_left(tree, get_operator(equ.curr()), prev_trees)
        return tree, equ, prev_trees, States.operator_unary_left

    elif equ.curr() in OPEN_PARENTHESES:
        equ, temp_tree = make_tree(equ)
        tree.set_left_tree(temp_tree)

        try:
            next(equ)
            equ.remove_white_space()
        except StopIteration:
            # if no next put tree in the middle
            tree = tree.get_left()
            return tree, equ, prev_trees, States.after_brackets
        if equ.curr() in CLOSE_PARENTHESES:
            # if close brackets put tree in the middle
            tree = tree.get_left()
            return tree, equ, prev_trees, States.close_brackets
        else:
            equ.prev()
            return tree, equ, prev_trees, States.after_brackets
    else:
        #Errors:
        if is_operator(equ.curr()):
            raise SyntaxError("Operator must be Unary left, instead got: " + equ.curr())
        elif equ.curr() in CLOSE_PARENTHESES:
            raise SyntaxError("Expecting operand: " + equ.curr())
        else:
            raise SyntaxError("Invalid Syntax: " + equ.curr())
