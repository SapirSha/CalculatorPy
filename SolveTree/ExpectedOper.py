from BinTree import BinTree
from Operand import Operand
from Operators.BinaryOperator import BinaryOperator
from Operators.UnaryLOperator import UnaryLOperator
from Operators.UnaryROperator import UnaryROperator
from SolveTree.ExpectedType import TREE_OPER

# check if the expected type and the instance are the same, if they are: return operand
def expected_operand(tree : BinTree):
    if isinstance(tree.get_info(), Operand):
        return tree.get_info()
    else:
        raise SyntaxError("Equation isn't finished, expecting an operand.")

# check if the expected type and the instance are the same, if they are: summon the operators function
def expected_operator_unary_right(tree : BinTree):
    from SolveTree.SolveTree import solve_tree
    if isinstance(tree.get_info()[TREE_OPER], UnaryROperator):
        return tree.get_info()[TREE_OPER].unary_r_operation(solve_tree(tree.get_left()))
    else:
        raise SyntaxError("Equation isn't finished, expecting an operand.")

# check if the expected type and the instance are the same, if they are: summon the operators function
def expected_operator_binary(tree : BinTree):
    from SolveTree.SolveTree import solve_tree
    if isinstance(tree.get_info()[TREE_OPER], BinaryOperator):
        return tree.get_info()[TREE_OPER].binary_operation(solve_tree(tree.get_left()), solve_tree(tree.get_right()))
    else:
        raise SyntaxError("Error: expected binary operator but got somthing else")  # should hypothetically never be reached but better safe than sorry

# check if the expected type and the instance are the same, if they are: summon the operators function
def expected_operator_unary_left(tree : BinTree):
    from SolveTree.SolveTree import solve_tree
    if isinstance(tree.get_info()[TREE_OPER], UnaryLOperator):
        return tree.get_info()[TREE_OPER].unary_l_operation(solve_tree(tree.get_right()))
    else:
        raise SyntaxError("Error: expected unary-left operator but got somthing else")  # should hypothetically never be reached but better safe than sorry