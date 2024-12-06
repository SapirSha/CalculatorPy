class Equation:
    _equation = None

    def __init__(self, equ):
        self._equation = equ
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.index += 1
            return self._equation[self.index]
        except IndexError as e:
            raise StopIteration

    def __repr__(self):
        return self._equation

    def curr(self):
        return self._equation[self.index]

    def prev(self):
        self.index -= 1
        return self._equation[self.index]


