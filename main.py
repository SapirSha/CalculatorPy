from Operators_Dictionary import operators_dictionary, create_operators_dictionary, is_operator, is_operator_binary, \
    is_operator_unary_l, is_operator_unary_r


def main():
    op = operators_dictionary
    for operator in op:
        print(operator)

    print(is_operator_unary_r('!'))

if __name__ == "__main__":
    main()