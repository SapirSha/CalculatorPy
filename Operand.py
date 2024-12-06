
class Operand:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

    def __add__(self, other):
        return self.data + other

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    @staticmethod
    def is_operand(c : str) -> bool:
        return c.isdigit()