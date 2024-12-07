import gettext

from BinTree import BinTree
from Equation import Equation
from Operators_Dictionary import *
from Stack import Stack
from Operand import Operand, is_operand

PRIO_AT_TREE = 1
OPERATOR_AT_TREE = 0

origin = BinTree()
cur = origin
tree_parents = Stack()
equ = Equation("")


def remove_white_space():
    global equ
    while next(equ).isspace():
        pass
    equ.prev()


def put_cur_at_appropriate_place(current_operator: Operator):
    global tree_parents, cur

    while (not tree_parents.is_empty()
           and tree_parents.peek().get_info()[PRIO_AT_TREE] >= current_operator.get_binary_priority()):
        cur = tree_parents.pop()


def put_cur_at_appropriate_place_r(current_operator: Operator):
    global tree_parents, cur
    while (not tree_parents.is_empty()
           and tree_parents.peek().get_info()[PRIO_AT_TREE] >= current_operator.get_unary_r_priority()):
        cur = tree_parents.pop()

def put_above_cur(operator : Operator, prio : int):
    global origin, cur, tree_parents

    if tree_parents.is_empty():
        cur = BinTree((get_operator(equ.curr()), prio), cur)
        origin = cur
    else:
        cur = tree_parents.pop()
        cur.set_right((get_operator(equ.curr()), prio), cur.get_right())
        tree_parents.push(cur)
        cur = cur.get_right()

def put_to_right_of_cur_and_check_out(operator: Operator, prio: int):
    global origin, cur, tree_parents

    cur.set_right((get_operator(equ.curr()), prio), cur.get_right())
    tree_parents.push(cur)
    cur = cur.get_right()


def init_tree():
    global origin, cur, tree_parents, equ

    origin = BinTree()
    cur = origin
    tree_parents = Stack()

    remove_white_space()
    if is_operand(next(equ)):
        cur.set_left(Operand(int(equ.curr())))
        while is_operand(next(equ)):
            cur.set_left(cur.get_left().get_info() * 10 + int(equ.curr()))
        equ.prev()

        remove_white_space()
        if is_operator(next(equ)):
            if is_operator_binary(equ.curr()):
                cur.set_info((get_operator(equ.curr()), get_operator(equ.curr()).get_binary_priority()))
            else:
                cur.set_info((get_operator(equ.curr()), get_operator(equ.curr()).get_unary_r_priority()))
        else:
            raise SyntaxError("Invalid Syntax (Expected Operator): '" + equ.curr() + "'")
        got_operator()
    elif is_operator_unary_l(equ.curr()):
        cur.set_info((get_operator(equ.curr()), get_operator(equ.curr()).get_unary_l_priority()))
        got_operator()
    elif is_operator(equ.curr()):
        raise SyntaxError("not a valid left operator: '" + equ.curr() + "'")
    else:
        raise SyntaxError("Syntax error: '" + equ.curr() + "'")


def got_operand():
    global origin, cur, tree_parents

    if is_operand(next(equ)):
        cur.get_right().set_info(cur.get_right().get_info() * 10 + int(equ.curr()))
        return got_operand()
    elif equ.curr().isspace():
        remove_white_space()
        next(equ)
    if is_operator(equ.curr()):
        if is_operator_binary(equ.curr()):
            put_cur_at_appropriate_place(get_operator(equ.curr()))
            if cur.get_info()[PRIO_AT_TREE] >= get_operator(equ.curr()).get_binary_priority():
                put_above_cur(get_operator(equ.curr()), get_operator(equ.curr()).get_binary_priority())
            else:
                put_to_right_of_cur_and_check_out(get_operator(equ.curr()), get_operator(equ.curr()).get_binary_priority())
            got_operator()
        elif is_operator_unary_r(equ.curr()):
            put_cur_at_appropriate_place_r(get_operator(equ.curr()))
            if cur.get_info()[PRIO_AT_TREE] >= get_operator(equ.curr()).get_unary_r_priority():
                put_above_cur(get_operator(equ.curr()), get_operator(equ.curr()).get_unary_r_priority())
            else:
                put_to_right_of_cur_and_check_out(get_operator(equ.curr()), get_operator(equ.curr()).get_unary_r_priority())
            got_operator()
        else:
            raise SyntaxError("not valid right or binary operator")
    else:
        raise SyntaxError("Expected Operator, instead got: '" + equ.curr() + "'")


def got_operator():
    global origin, cur, equ
    remove_white_space()

    if is_operand(next(equ)):
        cur.set_right(Operand(int(equ.curr())))
        got_operand()
    elif is_operator(equ.curr()):

        if is_operator_unary_r(equ.curr()):
            while is_operator_unary_r(equ.curr()):
                put_cur_at_appropriate_place_r(get_operator(equ.curr()))
                if isinstance(cur.get_info()[OPERATOR_AT_TREE], BinaryOperator) and cur.get_info()[PRIO_AT_TREE] >= get_operator(
                        equ.curr()).get_unary_r_priority():
                    if cur.get_info()[PRIO_AT_TREE] >= get_operator(equ.curr()).get_unary_r_priority():
                        put_above_cur(get_operator(equ.curr()), get_operator(equ.curr()).get_unary_r_priority())
                    else:
                        put_to_right_of_cur_and_check_out(get_operator(equ.curr()), get_operator(equ.curr()).get_binary_priority())
                elif isinstance(cur.get_info()[OPERATOR_AT_TREE], UnaryROperator):
                    if cur.get_info()[PRIO_AT_TREE] >= get_operator(equ.curr()).get_unary_r_priority():
                        put_above_cur(get_operator(equ.curr()), get_operator(equ.curr()).get_unary_r_priority())
                    else:
                        raise Exception("Somthing is wrong with the way the priorities are set up")
                remove_white_space()
                next(equ)
            if not tree_parents.is_empty():
                cur = tree_parents.pop()

        if equ.curr().isspace():
            remove_white_space()
            next(equ)

        if is_operator_binary(equ.curr()) and isinstance(cur.get_info()[OPERATOR_AT_TREE], UnaryROperator):
            put_cur_at_appropriate_place(get_operator(equ.curr()))
            if cur.get_info()[PRIO_AT_TREE] >= get_operator(equ.curr()).get_binary_priority():
                put_above_cur(get_operator(equ.curr()), get_operator(equ.curr()).get_binary_priority())
            else:
                put_to_right_of_cur_and_check_out(get_operator(equ.curr()), get_operator(equ.curr()).get_binary_priority())
        elif isinstance(cur.get_info()[OPERATOR_AT_TREE], BinaryOperator):
            if cur.get_right() is not None and isinstance(cur.get_right().get_info()[OPERATOR_AT_TREE], UnaryROperator):
                put_cur_at_appropriate_place(get_operator(equ.curr()))
                if cur.get_info()[PRIO_AT_TREE] >= get_operator(equ.curr()).get_binary_priority():
                    put_above_cur(get_operator(equ.curr()), get_operator(equ.curr()).get_binary_priority())
                else:
                    put_to_right_of_cur_and_check_out(get_operator(equ.curr()),
                                                      get_operator(equ.curr()).get_binary_priority())
            else:
                equ.prev()
        elif isinstance(cur.get_info()[OPERATOR_AT_TREE], BinaryOperator):
            pass
        else:
            raise SyntaxError("Expected binary operator")

        remove_white_space()
        if is_operator_unary_l(next(equ)):
            if cur.get_info()[PRIO_AT_TREE] < get_operator(equ.curr()).get_unary_l_priority():
                put_to_right_of_cur_and_check_out(get_operator(equ.curr()), get_operator(equ.curr()).get_unary_l_priority())
                while is_operator_unary_l(next(equ)) and cur.get_info()[PRIO_AT_TREE] <= get_operator(equ.curr()).get_unary_l_priority():
                    put_to_right_of_cur_and_check_out(get_operator(equ.curr()), get_operator(equ.curr()).get_unary_l_priority())
                    remove_white_space()
                if equ.curr().isspace():
                    remove_white_space()
                    next(equ)

                if is_operator_unary_l(equ.curr()) and cur.get_info()[PRIO_AT_TREE] > get_operator(equ.curr()).get_unary_l_priority():
                    raise Exception("Somthing is wrong with the priorities of some operators")
                elif not is_operand(equ.curr()):
                    raise SyntaxError("Incorrect usage of operators: " + equ.curr())
        equ.prev()
        got_operator()


def print_tree(tree: BinTree):
    if tree is None:
        return
    if isinstance(tree.get_info(), Operand):
        print(tree.get_info(), end=' ')
    else:
        print(tree.get_info()[OPERATOR_AT_TREE], end=' ')
    print_tree(tree.get_left())
    print_tree(tree.get_right())


def print_stack(stack: Stack):
    while not stack.is_empty():
        print(stack.pop().get_info(), end=' ')


def create_equation_tree(equation: Equation) -> BinTree:
    global equ

    equ = equation
    try:
        init_tree()
    except StopIteration:
        print("FINISHED EQUATION")

    return origin
