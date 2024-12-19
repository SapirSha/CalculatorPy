from Operand import Operand
from Operators.UnaryROperator import UnaryROperator
from SolveTree.CalculationError import CalculationError


class Hash(UnaryROperator):
    symbol = '#'
    unary_right_priority = 6

    def unary_r_operation(self, number: Operand) -> Operand:
        if number.get_data() < 0:
            raise CalculationError("Hash cannot be used with a negative number: " + str(number.get_data()))
        num = str(number.get_data())
        sum_of_digits = 0
        for digit in num:
            if digit.lower() == 'e':
                return Operand(sum_of_digits)
            elif digit != '.':
                sum_of_digits += int(digit)

        return Operand(sum_of_digits)
