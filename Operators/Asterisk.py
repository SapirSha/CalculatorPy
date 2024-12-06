from Operators.BinaryOperator import BinaryOperator


class Asterisk(BinaryOperator):
    symbol = '*'
    binary_priority = 2

    def binary_operation(self, left_operand, right_operand):
        return left_operand * right_operand