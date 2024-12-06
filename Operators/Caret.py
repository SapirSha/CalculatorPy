from math import pow

from Operators.BinaryOperator import BinaryOperator

class Caret(BinaryOperator):
    symbol = '^'
    binary_priority = 3

    def binary_operation(self, left_operand, right_operand):
        return pow(left_operand,right_operand)
