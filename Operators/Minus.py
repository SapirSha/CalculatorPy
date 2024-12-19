from Operand import Operand
from Operators.BinaryOperator import BinaryOperator
from Operators.UnaryLOperator import UnaryLOperator


class Minus(BinaryOperator, UnaryLOperator):
    symbol = '-'
    binary_priority = 1
    unary_left_priority = 2.5

    def binary_operation(self, left_operand: Operand, right_operand: Operand) -> Operand:
        return Operand(left_operand.get_data() - right_operand.get_data())

    def unary_l_operation(self, right_operand: Operand) -> Operand:
        return Operand(-1 * right_operand.get_data())
