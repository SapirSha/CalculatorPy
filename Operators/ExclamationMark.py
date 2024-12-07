from Operators.UnaryROperator import UnaryROperator


class ExclamationMark(UnaryROperator):
    symbol = '!'
    unary_right_priority = 6

    def unary_r_operation(self):
        ...