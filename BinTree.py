class BinTree:
    def __init__(self, info=None, left=None, right=None):
        self._left = left
        self._info = info
        self._right = right

    def set_left(self, info, left=None, right=None):
        self._left = BinTree(info, left, right)

    def set_left_tree(self, tree: 'BinTree'):
        self._left = tree

    def set_right(self, info, left=None, right=None):
        self._right = BinTree(info, left, right)

    def set_right_tree(self, tree: 'BinTree'):
        self._right = tree

    def set_info(self, info):
        self._info = info

    def get_left(self) -> 'BinTree':
        return self._left

    def get_right(self) -> 'BinTree':
        return self._right

    def get_info(self):
        return self._info
