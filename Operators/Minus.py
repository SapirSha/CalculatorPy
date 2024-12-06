from Operators.BinaryOperator import BinaryOperator
from Operators.UnaryLOperator import UnaryLOperator

class Minus(BinaryOperator, UnaryLOperator):
    symbol = '-'
    binary_priority = 1
    unary_left_priority = 6

    def binary_operation(self, left_operand, right_operand):
        return left_operand - right_operand

    def unary_l_operation(self, right_operand):
        return -right_operand