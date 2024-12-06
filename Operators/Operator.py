import Operators_Dictionary

class Operator:
    symbol = None

    def get_symbol(self):
        return self.symbol

    def __repr__(self):
        return self.symbol

    @staticmethod
    def is_operator(key : str) -> bool:
        return Operators_Dictionary.operators_dictionary.get(key) is not None