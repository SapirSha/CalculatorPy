from BinTree import BinTree
from Equation import Equation
from Operators_Dictionary import *
from Stack import Stack
from Operand import Operand, is_operand

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
           and get_operator(
                tree_parents.peek().get_info().get_symbol()).get_binary_priority() >= current_operator.get_binary_priority()):
        cur = tree_parents.pop()


def put_cur_at_appropriate_place_r(current_operator: Operator):
    global tree_parents, cur
    while (not tree_parents.is_empty()
           and get_operator(
                tree_parents.peek().get_info().get_symbol()).get_binary_priority() >= current_operator.get_unary_r_priority()):
        cur = tree_parents.pop()


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
            cur.set_info(get_operator(equ.curr()))
        else:
            raise SyntaxError("Invalid Syntax (Expected Operator): '" + equ.curr() + "'")
        got_operator()
    elif is_operator_unary_l(equ.curr()):
        cur.set_info(get_operator(equ.curr()))
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
            if cur.get_info().get_binary_priority() >= get_operator(equ.curr()).get_binary_priority():
                if tree_parents.is_empty():
                    cur = BinTree(get_operator(equ.curr()), cur)
                    origin = cur
                else:
                    cur = tree_parents.pop()
                    cur.set_right(get_operator(equ.curr()), cur.get_right())
                    tree_parents.push(cur)
                    cur = cur.get_right()
            else:
                cur.set_right(get_operator(equ.curr()), cur.get_right())
                tree_parents.push(cur)
                cur = cur.get_right()
            got_operator()
        elif is_operator_unary_r(equ.curr()):
            put_cur_at_appropriate_place_r(get_operator(equ.curr()))
            if cur.get_info().get_binary_priority() >= get_operator(equ.curr()).get_unary_r_priority():
                if tree_parents.is_empty():
                    cur = BinTree(get_operator(equ.curr()), cur)
                    origin = cur
                else:
                    cur = tree_parents.pop()
                    cur.set_right(get_operator(equ.curr()), cur.get_right())
                    tree_parents.push(cur)
                    cur = cur.get_right()
            else:
                cur.set_right(get_operator(equ.curr()), cur.get_right())
                tree_parents.push(cur)
                cur = cur.get_right()
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
    '''
    elif is_operator(equ.curr()):
        while current_is_operator_r():
            if not save_dad.is_empty() and dic_oper.get(save_dad.peek().get_info()) >= dic_oper.get(equ[index]):
                while not save_dad.is_empty() and dic_oper.get(save_dad.peek().get_info()) >= dic_oper.get(equ[index]):
                    cur = save_dad.pop()
                temp = BinTree(equ[index], cur)
                if save_dad.is_empty():
                    cur = temp
                    origin = cur
                else:
                    cur = save_dad.pop()
                    cur.set_right_tree(temp)
                    save_dad.push(cur)
                    cur = cur.get_right()
            else:
                temp = BinTree(equ[index], cur)
                if save_dad.is_empty():
                    cur = temp
                    origin = cur
                else:
                    cur = save_dad.pop()
                    cur.set_right_tree(temp)
                    save_dad.push(cur)
                    cur = cur.get_right()
            index += 1


        if current_is_operator_b() and prev_is_operator_r():
            print(save_dad.peek().get_info(), equ[index])
            while not save_dad.is_empty() and dic_oper_b.get(save_dad.peek().get_info()) >= dic_oper_b.get(equ[index]):
                cur = save_dad.pop()
            if dic_oper_b.get(cur.get_info()) >= dic_oper_b.get(equ[index]):
                temp = BinTree(equ[index], cur)
                if save_dad.is_empty():
                    cur = temp
                    origin = cur
                else:
                    cur = save_dad.pop()
                    cur.set_right_tree(temp)
                    save_dad.push(cur)
                    cur = cur.get_right()
            else:
                raise SyntaxError(" IDK MIGHT NO BE ERROR WILL SEE LATER")
        else:
            index -= 1
            if current_is_operator_b():
                print(cur.get_info(), equ[index])
                index -= 1
                if current_is_operator_r():
                    index += 1
                    if dic_oper_r.get(cur.get_info()) > dic_oper_b.get(equ[index]):
                        pass
                    else:
                        raise Exception("Somthing is wrong with the priority values (doing operation on operators)")
                else:
                    index += 1
            else:
                raise SyntaxError("no binary operator with unary operators")

        binary_operator = cur
        index += 1
        oper_left = 0
        while current_is_operator_l():
            if oper_left == 0 and dic_oper_l.get(equ[index]) > dic_oper.get(cur.get_info()):
                oper_left = 1
                cur.set_right(equ[index])
                save_dad.push(cur)
                cur = cur.get_right()
            elif oper_left != 0 and dic_oper_l.get(equ[index]) >= dic_oper_l.get(cur.get_info()):
                print_tree(cur)
                save_dad.push(cur)
                cur.set_right(equ[index])
                cur = cur.get_right()
            else:
                raise Exception("Somthing is wrong with the priority values (doing operation on operators)")
            index += 1

        if not current_is_operand():
            raise SyntaxError("Operand has to be after left operator")
        index -=1

        gotOperator()
    '''


def print_tree(tree: BinTree):
    if tree is None:
        return
    print(tree.get_info(), end=' ')
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
