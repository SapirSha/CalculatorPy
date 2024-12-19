from Equation import Equation
from Operators_Dictionary import DIC_PARENTHESES, OPEN_PARENTHESES, CLOSE_PARENTHESES
from Stack import Stack


# checks if the brackets are placed correctly
def count_parentheses(equ: Equation):
    brackets_stack = Stack()

    for char in equ:
        if char in OPEN_PARENTHESES or char in CLOSE_PARENTHESES:
            if char in OPEN_PARENTHESES:
                brackets_stack.push(char)
            elif char in CLOSE_PARENTHESES:
                if brackets_stack.is_empty():
                    equ.index = 0
                    raise SyntaxError("Missing Open parentheses (Invalid amount of closing brackets)")
                if DIC_PARENTHESES.get(brackets_stack.pop()) == char:
                    pass
                else:
                    raise SyntaxError("Incorrect parentheses placement ( brackets mashup )")

    if not brackets_stack.is_empty():
        raise SyntaxError("Missing Close parentheses (Invalid amount of closing brackets)")
