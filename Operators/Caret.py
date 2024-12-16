import math
from math import pow

from Operand import Operand
from Operators.BinaryOperator import BinaryOperator
from SolveTree.CalculationError import CalculationError


class Caret(BinaryOperator):
    symbol = '^'
    binary_priority = 3

    def binary_operation(self, left_operand :Operand, right_operand : Operand) -> Operand:
        try:
            # no idea if that is supposed to be a thing or not
            #if left_operand.get_data() == 0 and right_operand.get_data() == 0:
            #    raise CalculationError(" 0^0 is undefined")

            # math.pow results are kinda small, this if would check if the number is a certain amount so the calculator won't take a lot of time
            # in case the multiplication is too big do math.pow, so cases like 1 ^ (10^10) would still be one
            if right_operand.get_data() > 100000 or right_operand.get_data() * left_operand.get_data() > 100000000:
                return Operand(math.pow(left_operand.get_data(), right_operand.get_data()))
            return Operand(left_operand.get_data() ** right_operand.get_data())
        except OverflowError:
            raise CalculationError("Number in the equation is to big, trying to power: " + str(left_operand.get_data()) + ", by: " + str(right_operand.get_data()))
