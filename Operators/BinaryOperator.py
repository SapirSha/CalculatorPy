from Operators.Operator import Operator

class BinaryOperator(Operator):
    binary_priority = None

    def binary_operation(self, left_operand, right_operand):
        ...

    def get_binary_priority(self):
        return self.binary_priority

