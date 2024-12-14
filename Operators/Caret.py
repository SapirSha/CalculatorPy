from math import pow

from Operand import Operand
from Operators.BinaryOperator import BinaryOperator
from SolveTree.CalculationError import CalculationError


class Caret(BinaryOperator):
    symbol = '^'
    binary_priority = 3

    def binary_operation(self, left_operand :Operand, right_operand : Operand) -> Operand:
        try:
            return Operand(pow(left_operand.get_data(), right_operand.get_data()))
        except OverflowError:
            raise CalculationError("Number in the equation is to big, trying to power: " + str(left_operand.get_data()) + ", by: " + str(right_operand.get_data()))
