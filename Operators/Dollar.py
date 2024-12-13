from Operators.BinaryOperator import BinaryOperator


class Dollar(BinaryOperator):
    symbol = '$'
    binary_priority = 5

    def binary_operation(self, left_operand, right_operand):
        ...