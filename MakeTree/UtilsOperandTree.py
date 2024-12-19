from Equation import Equation
from Operand import Operand


# gets operand from equation (including floating point)
def get_operand_from_equ(equ: Equation) -> (Equation, Operand):
    number = ""
    float_flag = False
    try:
        while equ.curr().isdigit():
            number += equ.curr()
            next(equ)

        if equ.curr() == '.':
            number += equ.curr()
            float_flag = True
            try:
                if not next(equ).isdigit():
                    equ.prev()
                    raise SyntaxError("A floating point can only come inside an operand")
            except StopIteration:
                equ.prev()
                raise SyntaxError("A floating point can only come inside an operand")
            while equ.curr().isdigit():
                number += equ.curr()
                next(equ)
    except StopIteration:
        pass

    equ.prev()
    if float_flag:
        return equ, Operand(float(number))
    else:
        return equ, Operand(int(number))
