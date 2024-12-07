from abc import abstractmethod, ABC


class Operator(ABC):
    symbol = None

    def get_symbol(self):
        return self.symbol

    def __repr__(self):
        return self.symbol