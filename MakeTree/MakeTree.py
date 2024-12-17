from BinTree import BinTree
from Equation import Equation
from MakeTree.States import States
from Stack import Stack


# the function to handle the making of the tree
def make_tree(equ: Equation) -> (Equation, BinTree):
    tree = BinTree()
    prev_trees = Stack()
    state = States.start  # holds the appropriate function / 'state' depending on the previous char

    try:
        # while loop until StopIteration Exception
        while True:
            next(equ)
            tree, equ, prev, state = state(tree, equ, prev_trees)

    # stop the while loop
    except StopIteration:
        # do be worried to add an if statement and break for close brackets if want to change this exception
        pass
    # handle thrown syntax errors
    except SyntaxError as e:
        if e.msg is not None:
            print("<--- Error ------------------------------>")
            print(equ)
            print(equ.index * ' ' + '^')
            print(e)
            print("<---------------------------------------->")
        raise SyntaxError

    # get origin / the highest father / rank 0
    while not prev_trees.is_empty():
        tree = prev_trees.pop()

    return equ, tree
