class BinTree:
    def __init__(self, info, left = None, right = None):
        self._left = left
        self._info = info
        self._right = right

    def set_left(self, info, left = None, right = None):
        self._left = BinTree(info, left, right)

    def set_right(self, info, left = None, right = None):
        self._right = BinTree(info, left, right)

    def set_info(self, info):
        self._info = info

    def get_left(self) -> 'BinTree':
        return self._left

    def get_right(self) -> 'BinTree':
        return self._right

    def get_info(self):
        return self._info