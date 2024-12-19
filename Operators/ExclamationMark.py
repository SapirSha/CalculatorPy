from Operand import Operand
from Operators.UnaryROperator import UnaryROperator
from SolveTree.CalculationError import CalculationError


class ExclamationMark(UnaryROperator):
    symbol = '!'
    unary_right_priority = 6

    def unary_r_operation(self, number: Operand) -> Operand:
        if number.get_data() < 0:
            raise CalculationError("Cant factorial a negative number: " + str(number.get_data()))
        elif number.get_data() != int(number.get_data()):
            raise CalculationError("Cant factorial a floating point number: " + str(number.get_data()))
        if number.get_data() > 10000:
            raise CalculationError("Trying to factorial a number too big : " + str(number.get_data()))
        else:
            res = 1
            while number.get_data() > 1:
                res *= number.get_data()
                number.set_data(number.get_data() - 1)
            return Operand(res)
