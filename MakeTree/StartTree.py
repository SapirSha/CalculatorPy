from BinTree import BinTree
from Equation import Equation
from MakeTree.InsertToTree import insert_to_tree_operator_unary_right, insert_to_tree_operator_binary, \
    insert_to_tree_operator_unary_left, insert_to_tree_operand
from MakeTree.MakeTree import make_tree
from MakeTree.States import States
from Operand import is_operand, Operand
from Operators_Dictionary import is_operator_unary_l, is_operator, is_cur_operator_unary_r_in_equation, get_operator, \
    is_operator_binary
from Stack import Stack

def start_tree(tree : BinTree, equ : Equation, prev_trees : Stack) -> (BinTree, Equation, Stack, int):
    equ.remove_white_space()

    if is_operand(equ.curr()):
        temp = 0
        while is_operand(equ.curr()):
            temp = temp * 10 + int(equ.curr())
            next(equ)

        tree.set_left(Operand(temp))

        equ.remove_white_space()

        if is_cur_operator_unary_r_in_equation(equ):
            tree, prev_trees = insert_to_tree_operator_unary_right(tree, get_operator(equ.curr()), prev_trees)
            return tree, equ, prev_trees, States.operator_unary_right
        elif is_operator_binary(equ.curr()):
            tree, prev_trees = insert_to_tree_operator_binary(tree, get_operator(equ.curr()), prev_trees)
            return tree, equ, prev_trees, States.operator_binary
        elif is_operand(equ.curr()):
            raise SyntaxError("spaces between numbers are not allowed")
        else:
            raise SyntaxError("Incorrect syntax: " + equ.curr() + ", when expecting operator after operand")

    elif is_operator_unary_l(equ.curr()):
        tree, prev_trees = insert_to_tree_operator_unary_left(tree, get_operator(equ.curr()), prev_trees)

        return tree, equ, prev_trees, States.operator_unary_left

    elif equ.curr() == '(':
        equ, temp_tree = make_tree(equ)

        tree.set_left_tree(temp_tree)
        equ.remove_white_space()

        next(equ)
        equ.remove_white_space()

        if is_cur_operator_unary_r_in_equation(equ):
            tree, prev_trees = insert_to_tree_operator_unary_right(tree, get_operator(equ.curr()), prev_trees)
            return tree, equ, prev_trees, States.operator_unary_right
        elif is_operator_binary(equ.curr()):
            tree, prev_trees = insert_to_tree_operator_binary(tree, get_operator(equ.curr()), prev_trees)
            return tree, equ, prev_trees, States.operator_binary
        else:
            raise SyntaxError("Incorrect syntax: " + equ.curr() + ", when expecting operator after )")

    else:
        #Errors:
        if is_operator(equ.curr()):
            raise SyntaxError("Operator at start must be Unary left, instead got: " + equ.curr())
        elif equ.curr() == ')':
            raise SyntaxError("equation cannot start with close brackets: " + equ.curr())
        else:
            raise SyntaxError("Invalid Syntax: " + equ.curr())