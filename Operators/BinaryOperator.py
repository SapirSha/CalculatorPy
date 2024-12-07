from abc import ABC, abstractmethod

from Operators.Operator import Operator

class BinaryOperator(Operator, ABC):
    binary_priority = None

    @abstractmethod
    def binary_operation(self, left_operand, right_operand):
        ...



