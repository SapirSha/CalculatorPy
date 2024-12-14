from Operand import Operand
from Operators.BinaryOperator import BinaryOperator


class Asterisk(BinaryOperator):
    symbol = '*'
    binary_priority = 2

    def binary_operation(self, left_operand : Operand, right_operand : Operand) -> Operand:
        return Operand(left_operand.get_data() * right_operand.get_data())