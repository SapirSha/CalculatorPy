from Operators.BinaryOperator import BinaryOperator


class Asterisk(BinaryOperator):
    binary_priority = 2

    def binary_operation(self, left_operand, right_operand):
        return left_operand * right_operand

    def __repr__(self):
        return '*'