from BinTree import BinTree
from MakeTree.States import TREE_PRIO, TREE_OPER
from Operand import Operand
from Operators.BinaryOperator import BinaryOperator
from Operators.Minus import Minus
from Operators.Operator import Operator
from Operators.Tilde import Tilde
from Operators.UnaryROperator import UnaryROperator
from Operators_Dictionary import get_operator
from Stack import Stack


#searches the appropriate place and places the unary-right operator in the tree
def insert_to_tree_operator_unary_right(tree: BinTree, oper: Operator, prev_trees: Stack) -> (BinTree, Stack):
    #if empty place here
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_unary_r_priority()))

    #if operand place above
    elif isinstance(tree.get_info(), Operand):
        tree = BinTree((oper, oper.get_unary_r_priority()), tree)
        return tree, prev_trees

    else:
        # go up the tree
        while tree.get_info()[TREE_PRIO] >= oper.get_unary_r_priority() and not prev_trees.is_empty():
            tree = prev_trees.pop()

        # if the current node's operator is a higher or equal to priority of the one inserting: place above
        if tree.get_info()[TREE_PRIO] >= oper.get_unary_r_priority():
            tree = BinTree((oper, oper.get_unary_r_priority()), tree)
        # else place below
        else:
            tree.set_right((oper, oper.get_unary_r_priority()), tree.get_right())
            prev_trees.push(tree)
            tree = tree.get_right()

    return tree, prev_trees


#searches the appropriate place and places the binary operator in the tree
def insert_to_tree_operator_binary(tree: BinTree, oper: Operator, prev_trees: Stack) -> (BinTree, Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_binary_priority()))

    elif isinstance(tree.get_info(), Operand):
        tree = BinTree((oper, oper.get_binary_priority()), tree)
        return tree, prev_trees

    else:
        # go up the tree
        while tree.get_info()[TREE_PRIO] >= oper.get_binary_priority() and not prev_trees.is_empty():
            tree = prev_trees.pop()

        # if the current node's operator is a higher or equal to priority of the one inserting: place above
        if tree.get_info()[TREE_PRIO] >= oper.get_binary_priority():
            tree = BinTree((oper, oper.get_binary_priority()), tree)
        else:
            # if the current node's operator is unary - right: place above (in case operator unary - right is weaker than binary)
            if isinstance(tree.get_info()[TREE_OPER], UnaryROperator) and not isinstance(tree.get_info()[TREE_OPER], BinaryOperator):
                if prev_trees.is_empty():
                    tree = BinTree((oper, oper.get_binary_priority()), tree)
                    return tree, prev_trees
                else:
                    tree = prev_trees.pop()
            # else place below
            tree.set_right((oper, oper.get_binary_priority()), tree.get_right())
            prev_trees.push(tree)
            tree = tree.get_right()

    return tree, prev_trees


#searches the appropriate place and places the unary-left operator in the tree
def insert_to_tree_operator_unary_left(tree: BinTree, oper: Operator, prev_trees: Stack) -> (BinTree, Stack):
    if tree.get_info() is None:
        tree.set_info((oper, oper.get_unary_l_priority()))
    elif isinstance(tree.get_info(), Operand):
        tree = BinTree((oper, oper.get_unary_l_priority()), tree)
        return tree, prev_trees
    else:
        ### doesn't go up the tree because it comes after operator binary in equation but needs to work before it, no matter the priority
        ## Unique situation:
        # if current tree's node is tilde, another operator cannot come after it, apart from unary minus
        if isinstance(tree.get_info()[TREE_OPER], Tilde) and not isinstance(oper, Minus):
            raise SyntaxError(
                "Operator Tilde(~) must come before a number, unary minus or (, instead got: " + oper.get_symbol())
        # if current tree's node is NOT minus unary, and trying to a unary minus, place an (Assigned minus) that is 'a part' of the number
        elif isinstance(oper, Minus) and not (
                isinstance(tree.get_info()[TREE_OPER], Minus) and tree.get_info()[TREE_PRIO] == get_operator(
                '-').get_unary_l_priority()):
            tree.set_right((oper, "Assigned Minus"), None, tree.get_right())
        # if current tree's node is minus unary, can only insert another minus unary
        elif isinstance(tree.get_info()[TREE_OPER], Minus) and tree.get_info()[TREE_PRIO] == get_operator(
                '-').get_unary_l_priority() and not isinstance(oper, Minus):
            raise SyntaxError(
                "Operator Unary Minus must come before a number, another minus or (, instead got: " + oper.get_symbol())
        else:
            # for more general cases
            if tree.get_right() is None or not isinstance(tree.get_right().get_info()[TREE_OPER], Minus):
                tree.set_right((oper, oper.get_unary_l_priority()), tree.get_right())
                prev_trees.push(tree)
                tree = tree.get_right()

    return tree, prev_trees


#searches the appropriate place and places the operand in the tree
def insert_to_tree_operand(tree: BinTree, oper: Operand, prev_trees: Stack) -> None:
    # goes to the right most place and places the operand there, only needed in cases of unary-left operators
    while tree.get_right() is not None and not isinstance(tree.get_right().get_info(), Operand):
        tree = tree.get_right()
    if tree.get_right() is None:
        tree.set_right(oper)
    else:
        # shouldn't be reached, but in case, expand the operand
        tree.set_right(tree.get_right().get_info() * 10 + oper.get_data())


#searches the appropriate place and places a tree in the tree
def insert_to_tree_tree(tree: BinTree, ttree: BinTree, prev_trees: Stack) -> None:
    # goes to the right most leaf and places the tree
    while tree.get_right() is not None:
        tree = tree.get_right()
    tree.set_right_tree(ttree)
