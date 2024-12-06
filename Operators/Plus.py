from Operators.BinaryOperator import BinaryOperator

class Plus(BinaryOperator):
    symbol = '+'
    binary_priority = 1

    def binary_operation(self, left_operand, right_operand):
        return left_operand + right_operand


