from Equation import Equation
from Operand import Operand, is_operand


def get_operand_from_equ(equ : Equation) -> (Equation, Operand):
    temp = 0
    try:
        while is_operand(equ.curr()):
            temp = temp * 10 + int(equ.curr())
            next(equ)
    except StopIteration:
        equ.prev()
        return equ, Operand(temp)

    if equ.curr() == '.':
        try:
            next(equ)
            if not is_operand(equ.curr()):
                equ.prev()
                raise SyntaxError("A number cannot end with '.' ")
        except StopIteration:
            equ.prev()
            raise SyntaxError("A number cannot end with '.' ")
        temp2 = 0
        count = 0
        try:
            while is_operand(equ.curr()):
                temp2 = temp2 * 10 + int(equ.curr())
                count += 1
                next(equ)
        except StopIteration:
            pass

        number = temp + (temp2/10 ** count)
    else:
        number = temp

    equ.prev()
    return equ, Operand(number)
