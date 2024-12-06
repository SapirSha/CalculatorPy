from abc import ABC
import Operators_Dictionary


class Operator(ABC):
    ...
    @staticmethod
    def is_operator(key : str) -> bool:
        return Operators_Dictionary.operators_dictionary.get(key) is not None

