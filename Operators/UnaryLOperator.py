from Operators.Operator import Operator

class UnaryLOperator(Operator):
    unary_left_priority = None

    def unary_l_operation(self, number):
        pass

    def get_unary_l_priority(self):
        return self.unary_left_priority