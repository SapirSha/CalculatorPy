from abc import ABC, abstractmethod

from Operators.Operator import Operator

class UnaryROperator(Operator, ABC):
    unary_right_priority = None

    @abstractmethod
    def unary_r_operation(self):
        ...

    def get_unary_r_priority(self) -> int:
        return self.unary_right_priority
