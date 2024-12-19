from Operand import Operand
from Operators.UnaryLOperator import UnaryLOperator


class Tilde(UnaryLOperator):
    symbol = '~'
    unary_left_priority = 6

    def unary_l_operation(self, number: Operand) -> Operand:
        return Operand(-1 * number.get_data())
