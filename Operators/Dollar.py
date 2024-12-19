from Operand import Operand
from Operators.BinaryOperator import BinaryOperator


class Dollar(BinaryOperator):
    symbol = '$'
    binary_priority = 5

    def binary_operation(self, left_operand: Operand, right_operand: Operand) -> Operand:
        return Operand(max(left_operand.get_data(), right_operand.get_data()))
