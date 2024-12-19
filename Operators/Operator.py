from abc import abstractmethod, ABC

from Operators.Singleton import Singleton


class Operator(ABC, Singleton):
    symbol = None
    binary_priority = 0
    unary_left_priority = 0
    unary_right_priority = 0

    def get_symbol(self):
        return self.symbol

    def __repr__(self):
        return self.symbol

    def get_max_prio(self):
        return max(self.binary_priority, self.unary_left_priority, self.unary_right_priority)

    def get_unary_r_priority(self):
        return self.unary_right_priority

    def get_unary_l_priority(self):
        return self.unary_left_priority

    def get_binary_priority(self):
        return self.binary_priority