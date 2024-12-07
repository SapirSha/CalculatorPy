from Operators.BinaryOperator import BinaryOperator


class Slash(BinaryOperator):
    symbol = '/'
    binary_priority = 2

    def binary_operation(self, left_operand, right_operand):
        ...