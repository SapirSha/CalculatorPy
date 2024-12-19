# a class to hold the equation and iterate through it
class Equation:
    _equation = None

    def __init__(self, equ: str):
        self._equation = equ
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self) -> str:
        try:
            self.index += 1
            return self._equation[self.index]
        except IndexError as e:
            raise StopIteration

    def __repr__(self) -> str:
        return self._equation

    def curr(self) -> str:
        return self._equation[self.index]

    def prev(self) -> str:
        self.index -= 1
        return self._equation[self.index]

    def get(self, index) -> str:
        return self._equation[index]

    # get the next non-white char (without moving index)
    def next_non_space(self) -> str:
        i = self.index
        try:
            while self._equation[i + 1].isspace():
                i += 1
            return self._equation[i + 1]
        except IndexError as e:
            raise StopIteration

    # get the next non-white char (and mov the index there)
    def remove_white_space(self):
        try:
            while self.curr().isspace():
                self.index += 1
        except IndexError:
            raise StopIteration
