from abc import ABC, abstractmethod

from Operand import Operand
from Operators.Operator import Operator

class UnaryROperator(Operator, ABC):
    unary_right_priority = None

    @abstractmethod
    def unary_r_operation(self, number : Operand) -> Operand:
        ...


