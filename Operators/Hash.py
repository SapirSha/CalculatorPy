from Operand import Operand
from Operators.UnaryROperator import UnaryROperator


class Hash(UnaryROperator):
    symbol = '#'
    unary_right_priority = 6

    def unary_r_operation(self, number : Operand) -> Operand:
        num = str(number.get_data())
        sum_of_digits = 0
        for digit in num:
            if digit != '.':
                sum_of_digits += int(digit)

        return Operand(sum_of_digits)