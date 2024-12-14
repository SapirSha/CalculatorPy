from BinTree import BinTree
from Equation import Equation
from Operand import is_operand
from Operators.BinaryOperator import BinaryOperator
from Operators.UnaryLOperator import UnaryLOperator
from Operators.UnaryROperator import UnaryROperator
from Operators_Dictionary import get_operator, OPEN_BRACKETS, CLOSE_BRACKETS


def is_operator(symbol: str) -> bool:
    return get_operator(symbol) is not None


def is_operator_binary(symbol: str) -> bool:
    return is_operator(symbol) and isinstance(get_operator(symbol), BinaryOperator)


def is_operator_unary_l(symbol: str) -> bool:
    return is_operator(symbol) and isinstance(get_operator(symbol), UnaryLOperator)


def is_operator_unary_r(symbol: str) -> bool:
    return is_operator(symbol) and isinstance(get_operator(symbol), UnaryROperator)


def is_cur_operator_unary_r_in_equation(equ: Equation) -> bool:
    current = equ.curr()

    if not is_operator_unary_r(current):
        return False
    elif not is_operator_binary(current):
        return True
    try:
        next_symb = equ.next_non_space()
    except StopIteration:
        return True
    if is_operand(next_symb):
        return False
    elif next_symb in OPEN_BRACKETS:
        return False
    elif next_symb in CLOSE_BRACKETS:
        return True
    elif not is_operator(next_symb):
        raise SyntaxError("Invalid Syntax: " + next_symb)

    # compare with the next operator
    oper_current = get_operator(current)
    oper_next = get_operator(next_symb)
    if (isinstance(oper_next, UnaryROperator) or isinstance(oper_next, BinaryOperator)) and not isinstance(oper_next, UnaryLOperator):
        return True
    else:
        prio_left, prio_bin, prio_right = oper_next.get_unary_l_priority(), oper_next.get_binary_priority(), oper_next.get_unary_r_priority()
        if max(oper_current.get_unary_r_priority(), prio_left, prio_bin, prio_right) == prio_left:
            return False # This is somewhat troublesome
        else:
            return True