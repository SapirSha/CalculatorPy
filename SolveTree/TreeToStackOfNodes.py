from BinTree import BinTree
from Stack import Stack


def get_trees_internal_nodes(tree : BinTree) -> Stack:
    if tree is None or tree.get_info() is None:
        raise SyntaxError("Empty Equation!")

    tree_stack = Stack()
    tree_stack.push(tree)

    nodes = Stack()

    while not tree_stack.is_empty():
        tree = tree_stack.pop()

        if tree.get_right() is not None or tree.get_left() is not None:
            nodes.push(tree)

            if tree.get_left() is not None:
                tree_stack.push(tree.get_left())
            if tree.get_right() is not None:
                tree_stack.push(tree.get_right())

    return nodes