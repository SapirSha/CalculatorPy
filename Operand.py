
class Operand:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

    @staticmethod
    def is_operand(c : str) -> bool:
        return c.isdigit()