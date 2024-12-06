from Operators.BinaryOperator import BinaryOperator

class Plus(BinaryOperator):
    binary_priority = 1

    def binary_operation(self, left_operand, right_operand):
        return left_operand + right_operand

    def __repr__(self):
        return '+'

