class StackType:
    def __init__(self, info=None, next=None):
        self.info = info
        self.next = next


class Stack:
    def __init__(self, stack=StackType()):
        self.stack = stack

    def is_empty(self):
        return self.stack.info is None

    def push(self, info):
        self.stack = StackType(info, self.stack)

    def pop(self):
        t = self.stack.info
        self.stack = self.stack.next
        return t

    def peek(self):
        return self.stack.info

    def clear(self):
        self.stack = StackType()