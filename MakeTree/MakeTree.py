from BinTree import BinTree
from Equation import Equation
from MakeTree.InsertToTree import insert_to_tree_operand, insert_to_tree_tree
from MakeTree.States import States
from Stack import Stack

def print_tree(tree : BinTree):
    if tree is None:
        return
    print(tree.get_info(), end = ' ')
    print_tree(tree.get_left())
    print_tree(tree.get_right())


def make_tree(equ : Equation) -> (Equation, BinTree):
    from MakeTree.OperandTree import operand_tree
    from MakeTree.OperatorBinaryTree import operator_binary_tree
    from MakeTree.OperatorUnaryLeftTree import operator_unary_left_tree
    from MakeTree.OperatorUnaryRight import operator_unary_right_tree
    from MakeTree.StartTree import start_tree

    tree = BinTree()
    prev_trees = Stack()
    state = States.start

    try:
        while True:
            next(equ)
            if state == States.start:
                tree, equ, prev_trees, state = start_tree(tree, equ, prev_trees)
            elif state == States.operator_binary:
                tree, equ, prev_trees, state = operator_binary_tree(tree, equ, prev_trees)
            elif state == States.operator_unary_right:
                tree, equ, prev_trees, state = operator_unary_right_tree(tree, equ, prev_trees)
            elif state == States.operator_unary_left:
                tree, equ, prev_trees, state = operator_unary_left_tree(tree, equ, prev_trees)
            elif state == States.operand:
                tree, equ, prev_trees, state = operand_tree(tree, equ, prev_trees)
            elif state == States.open_brackets:
                equ.prev()
                equ, temp_tree = make_tree(equ)
                insert_to_tree_tree(tree ,temp_tree, prev_trees)
                state = States.operand
            elif state == States.close_brackets:
                equ.prev()
                print("Brackets close")
                break
            else:
                break

    except StopIteration:
        print("STOP")
    except SyntaxError as e:
        print(e)


    while not prev_trees.is_empty():
        tree = prev_trees.pop()
    print_tree(tree)

    return equ, tree