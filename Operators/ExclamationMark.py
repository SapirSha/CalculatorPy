from Operand import Operand
from Operators.UnaryROperator import UnaryROperator


class ExclamationMark(UnaryROperator):

    symbol = '!'
    unary_right_priority = 6

    def unary_r_operation(self, number : Operand) -> Operand:
        if number.get_data() < 0:
            raise SyntaxError(" cant factorial a negative number")
        elif number.get_data() != int(number.get_data()):
            raise SyntaxError(" cant factorial a floating point number")
        else:
            res = 1
            while number.get_data() > 1:
                res *= number.get_data()
                number.set_data(number.get_data() - 1)
            return Operand(res)