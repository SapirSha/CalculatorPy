from BinTree import BinTree
from Stack import Stack

equ = ("5+7!+-3+1")
index = 0

dic_oper = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3,
    '%': 4,
    '$': 5,
    '&': 5,
    '@': 5,
    '~': 6,
    '!': 6,
}
dic_oper_r = {
    '!': 6
}
dic_oper_l = {
    '-': 6,
    '~': 6
}

origin = BinTree()
cur = origin
save_dad = Stack()

def current_is_binary():
    return cur.get_left() is not None and cur.get_right() is not None

def current_is_unary_left():
    return cur.get_left() is None and cur.get_right() is not None

def current_is_operand():
    return equ[index].isdigit()


def current_is_operator():
    return dic_oper.get(equ[index]) is not None

def current_is_operator_b():
    return current_is_operator() and dic_oper_r.get(equ[index]) is None and  dic_oper_l.get(equ[index]) is None

def current_is_operator_l():
    return dic_oper_l.get(equ[index]) is not None

def current_is_operator_r():
    return dic_oper_r.get(equ[index]) is not None



def gotOperand():
    global index, equ, origin, cur
    index += 1

    if current_is_operand():
        cur.set_right(int(cur.get_right().get_info()) * 10 + int(equ[index]))
        gotOperand()
    elif current_is_operator(): # has to be binary or right
        if current_is_binary():
            if dic_oper.get(cur.get_info()) < dic_oper.get(equ[index]):
                cur.set_right_tree(BinTree(equ[index], cur.get_right()))
                save_dad.push(cur)
                cur = cur.get_right()
            else:
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
        elif current_is_unary_left():
            if dic_oper_l.get(cur.get_info()) < dic_oper.get(equ[index]):
                cur.set_right_tree(BinTree(equ[index], cur.get_right()))
                save_dad.push(cur)
                cur = cur.get_right()
            else:
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

        gotOperator()
    else:
        raise SyntaxError("Syntax not good")


def gotOperator():
    global index, equ, origin, cur
    index += 1

    if current_is_operand():
        cur.set_right(int(equ[index]))
        gotOperand()
    elif current_is_operator():
        start_operator = cur
        while current_is_operator_r():
            if not save_dad.is_empty() and dic_oper.get(save_dad.peek().get_info()) >= dic_oper.get(equ[index]):
                raise Exception("Somthing is wrong with the priority values")
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


        if current_is_operator_b():
            if dic_oper_r.get(cur.get_info()) > dic_oper.get(equ[index]):
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
                raise Exception("Somthing is wrong with the priority values")
        else:
            index -= 1
            if current_is_operator_b():
                if dic_oper.get(cur.get_info()) > dic_oper.get(equ[index]):
                    pass
                else:
                    raise Exception("Somthing is wrong with the priority values (doing operation on operators)")
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
                save_dad.push(cur)
                cur = cur.get_right()
                cur.set_right(equ[index])
            else:
                raise Exception("Somthing is wrong with the priority values (doing operation on operators)")
            index += 1

        if not current_is_operand():
            raise SyntaxError("Operand has to be after left operator")
        index -=1

        gotOperator()
    else:
        raise SyntaxError("Syntax not good")


def start():
    global index, equ, origin, cur

    if current_is_operand():
        cur.set_left(int(equ[index]))
        index += 1
        cur.set_info(equ[index])
        index += 1
        cur.set_right(int(equ[index]))
        gotOperand()
    elif current_is_operator(): #### is left operator
        cur.set_info(equ[index])
        gotOperator()
    else:
        raise SyntaxError(" Not Good Syntax! ")


def print_tree(tree: BinTree):
    if tree is None:
        return
    print(tree.get_info(), end = ' ')
    print_tree(tree.get_left())
    print_tree(tree.get_right())

def print_stack(stack : Stack):
    while not stack.is_empty():
        print(stack.pop().get_info(), end = ' ')

def main():
    try:
        start()
    except IndexError as e:
        print(e)
    print(equ)
    print_tree(origin)
    print("\nSTACK: ")
    print_stack(save_dad)

main()