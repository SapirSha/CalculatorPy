from BinTree import BinTree
from Equation import Equation
from MakeTree.States import States
from Stack import Stack


def make_tree(equ: Equation) -> (Equation, BinTree):


    tree = BinTree()
    prev_trees = Stack()
    state = States.start

    try:
        while True:
            next(equ)
            if state == States.close_brackets:
                equ.prev()
                break
            else:
                tree, equ, prev, state = state(tree, equ, prev_trees)


    except StopIteration:
        pass
    except SyntaxError as e:
        if e.msg is not None:
            print(equ.index * ' ' + '^')
            print(e.msg)
        raise SyntaxError

    while not prev_trees.is_empty():
        tree = prev_trees.pop()

    return equ, tree
