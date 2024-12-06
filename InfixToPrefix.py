from BinTree import BinTree
from Stack import Stack


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

equ = "5*7-~4"
index = 0

origin = BinTree()
cur = origin
save_dad = Stack()

def current_is_operand():
    return equ[index].isdigit()


def current_is_operator():
    return dic_oper.get(equ[index]) is not None



def Operand():
    global index, equ, origin, cur
    index += 1

    if current_is_operand():
        cur.set_right(int(cur.get_right().get_info()) * 10 + int(equ[index]))
        Operand()
    elif current_is_operator():
        if dic_oper.get(cur.get_info()) < dic_oper.get(equ[index]):
            cur.set_right_tree(BinTree(equ[index], cur.get_right()))
            save_dad.push(cur)
            cur = cur.get_right()
        else:
            while not save_dad.is_empty() and dic_oper.get(save_dad.peek().get_info()) >= dic_oper.get(equ[index]):
                cur = save_dad.pop()
            temp = BinTree(equ[index], cur)
            cur = temp
            if save_dad.is_empty():
                origin = cur
        Operator()
    else:
        raise SyntaxError("Syntax not good")


def Operator():
    global index, equ, origin, cur
    index += 1

    if current_is_operand():
        cur.set_right(int(equ[index]))
        Operand()
    elif current_is_operator():
        while not save_dad.is_empty() and dic_oper.get(save_dad.peek().get_info()) >= dic_oper.get(equ[index]):
            cur = save_dad.pop()
        if dic_oper.get(cur.get_info()) < dic_oper.get(equ[index]):
            cur.set_right(equ[index])
            cur = cur.get_right()
        else:
            temp = BinTree(equ[index], cur)
            cur = temp
            if save_dad.is_empty():
                origin = cur
        Operator()
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
        Operand()
    elif current_is_operator(): #### is left operator
        cur.set_info(equ[index])
        Operator()
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