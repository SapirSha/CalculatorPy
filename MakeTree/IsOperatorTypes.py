from BinTree import BinTree
from Equation import Equation
from Operand import is_operand
from Operators.BinaryOperator import BinaryOperator
from Operators.UnaryLOperator import UnaryLOperator
from Operators.UnaryROperator import UnaryROperator
from Operators_Dictionary import get_operator


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
    elif next_symb == '(':
        return False
    elif next_symb == ')':
        return True
    elif not is_operator(next_symb):
        raise SyntaxError("Invalid Symbol: " + next_symb)

    # compare with the next operator
    operc = get_operator(current)
    opern = get_operator(next_symb)
    if (isinstance(opern, UnaryROperator) or isinstance(opern, BinaryOperator)) and not isinstance(opern,
                                                                                                   UnaryLOperator):
        return True
    else:
        priol, priob, prior = opern.get_unary_l_priority(), opern.get_binary_priority(), opern.get_unary_r_priority()
        if max(operc.get_unary_r_priority(), priol, priob, prior) == priol:
            return False
        else:
            return True