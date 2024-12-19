from Equation import Equation
from Operand import is_operand
from Operators.BinaryOperator import BinaryOperator
from Operators.UnaryLOperator import UnaryLOperator
from Operators.UnaryROperator import UnaryROperator
from Operators_Dictionary import get_operator, CLOSE_PARENTHESES, OPEN_PARENTHESES


def is_operator(symbol: str) -> bool:
    return get_operator(symbol) is not None


def is_operator_binary(symbol: str) -> bool:
    return is_operator(symbol) and isinstance(get_operator(symbol), BinaryOperator)


def is_operator_unary_l(symbol: str) -> bool:
    return is_operator(symbol) and isinstance(get_operator(symbol), UnaryLOperator)


def is_operator_unary_r(symbol: str) -> bool:
    return is_operator(symbol) and isinstance(get_operator(symbol), UnaryROperator)


# this function predicts the operator type:
#   this function is important in cases where the operator is both unary-right and binary while the two priorities are different
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

    # check what is the next symbol
    if is_operand(next_symb):
        return False
    elif next_symb in OPEN_PARENTHESES:
        return False
    elif next_symb in CLOSE_PARENTHESES:
        return True
    elif not is_operator(next_symb):
        raise SyntaxError("Invalid Syntax: " + next_symb)

    # compare with the next symbol(operator)
    oper_current = get_operator(current)
    oper_next = get_operator(next_symb)
    # if the next symbol can only be binary or unary right, both cases make the current operator unary right
    if (isinstance(oper_next, UnaryROperator) or isinstance(oper_next, BinaryOperator)) and not isinstance(oper_next,
                                                                                                           UnaryLOperator):
        return True
    else:
        prio_left, prio_bin, prio_right = oper_next.get_unary_l_priority(), oper_next.get_binary_priority(), oper_next.get_unary_r_priority()
        if max(oper_current.get_unary_r_priority(), prio_left, prio_bin, prio_right) == prio_left and max(
                oper_current.get_unary_r_priority(), prio_bin, prio_right) != prio_left:
            return False  # This is somewhat troublesome but very rare (impossible in current operators versions)
        else:
            return True
