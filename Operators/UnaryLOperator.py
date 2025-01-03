from abc import ABC, abstractmethod

from Operand import Operand
from Operators.Operator import Operator


class UnaryLOperator(Operator, ABC):
    unary_left_priority = None

    @abstractmethod
    def unary_l_operation(self, number: Operand) -> Operand:
        ...
