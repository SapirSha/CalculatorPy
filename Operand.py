def is_operand(c: str):
    return c.isdigit() or c == '.'

# wrapper for a number
class Operand:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

    def __add__(self, param):
        return Operand(self.get_data() + param)

    def __mul__(self, param):
        return Operand(self.get_data() * param)

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data
