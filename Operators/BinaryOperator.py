from abc import ABC, abstractmethod

from Operand import Operand
from Operators.Operator import Operator


class BinaryOperator(Operator, ABC):
    binary_priority = None

    @abstractmethod
    def binary_operation(self, left_operand: Operand, right_operand: Operand) -> Operand:
        ...
