from BinTree import BinTree
from Operand import is_operand, Operand
from Operators.BinaryOperator import BinaryOperator
from Operators.Operator import Operator
from Operators.UnaryLOperator import UnaryLOperator
from Operators.UnaryROperator import UnaryROperator
from Operators_Dictionary import get_operator
from SolveTree.GetExpectedType import get_expected_type
from SolveTree.ExpectedType import ExpectedType, TREE_OPER


def solve_tree(tree : BinTree):
    expected_type = get_expected_type(tree)
    if expected_type == ExpectedType.operand:
        if isinstance(tree.get_info(), Operand):
            return tree.get_info()
        else:
            print(tree.get_info())
            raise SyntaxError(" This one's not operand?")
    elif expected_type == ExpectedType.operator_binary:
        if isinstance(tree.get_info()[TREE_OPER], BinaryOperator):
            return tree.get_info()[TREE_OPER].binary_operation(solve_tree(tree.get_left()), solve_tree(tree.get_right()))
        else:
            raise SyntaxError("not binary?")
    elif expected_type == ExpectedType.operator_unary_left:
        if isinstance(tree.get_info()[TREE_OPER], UnaryLOperator):
            return tree.get_info()[TREE_OPER].unary_l_operation(solve_tree(tree.get_right()))
        else:
            raise SyntaxError(" not unary left?")
    elif expected_type == ExpectedType.operator_unary_right:
        if isinstance(tree.get_info()[TREE_OPER], UnaryROperator):
            return tree.get_info()[TREE_OPER].unary_r_operation(solve_tree(tree.get_left()))
        else:
            raise SyntaxError("not unary right?")


