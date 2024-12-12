from BinTree import BinTree
from CreateEquationTree import print_tree
from Equation import Equation
from MakeTree.StartTree import start_tree
from MakeTree.States import States
from Stack import Stack


def make_tree(equ : Equation) -> (Equation, BinTree):
    tree = BinTree()
    prev_trees = Stack()
    state = States.start

    try:
        while True:
            if state == States.start:
                tree, equ, prev_trees, state = start_tree(tree, equ, prev_trees)
            elif state == States.operator_binary:
                print("Binary")
                break
            elif state == States.operator_unary_right:
                print("right")
                break
            elif state == States.operator_unary_left:
                print("left")
                break

    except StopIteration:
        print("STOP")
    except SyntaxError as e:
        print(e)

    print_tree(tree)
    return equ, tree