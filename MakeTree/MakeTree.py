from BinTree import BinTree
from Equation import Equation
from MakeTree.OperandTree import operand_tree
from MakeTree.OperatorUnaryLeftTree import operator_unary_left_tree
from MakeTree.StartTree import start_tree
from MakeTree.States import States
from Stack import Stack

def print_tree(tree : BinTree):
    if tree is None:
        return
    print(tree.get_info(), end = ' ')
    print_tree(tree.get_left())
    print_tree(tree.get_right())


def make_tree(equ : Equation) -> (Equation, BinTree):
    tree = BinTree()
    prev_trees = Stack()
    state = States.start

    try:
        while True:
            next(equ)
            if state == States.start:
                tree, equ, prev_trees, state = start_tree(tree, equ, prev_trees)
            elif state == States.operator_binary:
                print("Binary")
                break
            elif state == States.operator_unary_right:
                print("right")
                break
            elif state == States.operator_unary_left:
                tree, equ, prev_trees, state = operator_unary_left_tree(tree, equ, prev_trees)
            elif state == States.operand:
                tree, equ, prev_trees, state = operand_tree(tree, equ, prev_trees)

    except StopIteration:
        print("STOP")
    except SyntaxError as e:
        print(e)


    while not prev_trees.is_empty() and not prev_trees.is_last_one():
        prev_trees.pop()
    if prev_trees.is_empty():
        print_tree(tree)
    else:
        print_tree(prev_trees.peek())


    return equ, tree