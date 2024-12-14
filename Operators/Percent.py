from Operand import Operand
from Operators.BinaryOperator import BinaryOperator
from SolveTree.CalculationError import CalculationError


class Percent(BinaryOperator):
    symbol = '%'
    binary_priority = 4

    def binary_operation(self, left_operand : Operand, right_operand : Operand) -> Operand:
        if right_operand.get_data() == 0:
            raise CalculationError("Modulo by zero is undefined: " + str(left_operand.get_data()) + " % " + str(right_operand.get_data()))
        return Operand(left_operand.get_data() % right_operand.get_data())