from Equation import Equation
from Operators_Dictionary import DIC_BRACKETS, OPEN_BRACKETS, CLOSE_BRACKETS
from Stack import Stack



def count_brackets(equ : Equation):
    brackets_stack = Stack()


    for char in equ:
        if DIC_BRACKETS.get(char) is not None:
            if char in OPEN_BRACKETS:
                brackets_stack.push(char)
            elif char in CLOSE_BRACKETS:
                if brackets_stack.is_empty():
                    equ.index = 0
                    raise SyntaxError("Missing Open Brackets")
                if DIC_BRACKETS.get(brackets_stack.pop()) == char:
                    pass
                else:
                    raise SyntaxError("Incorrect Brackets Placement")

    if not brackets_stack.is_empty():
        raise SyntaxError("Missing Close Brackets")