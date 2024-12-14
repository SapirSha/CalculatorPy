from Operators.BinaryOperator import BinaryOperator
from Operators.UnaryROperator import UnaryROperator


class Hash(UnaryROperator):
    symbol = '#'
    unary_right_priority = 6

    def unary_r_operation(self):
        ...