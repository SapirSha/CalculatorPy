from Operators.BinaryOperator import BinaryOperator


class Percent(BinaryOperator):
    symbol = '%'
    binary_priority = 4

    def binary_operation(self, left_operand, right_operand):
        ...