from Operators.UnaryLOperator import UnaryLOperator


class Tilde(UnaryLOperator):
    symbol = '~'
    unary_left_priority = 6

    def unary_l_operation(self, number):
        ...