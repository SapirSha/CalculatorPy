from math import pow

from Operand import Operand
from Operators.BinaryOperator import BinaryOperator

class Caret(BinaryOperator):
    symbol = '^'
    binary_priority = 3

    def binary_operation(self, left_operand :Operand, right_operand : Operand) -> Operand:
        return Operand(pow(left_operand.get_data(), right_operand.get_data()))
