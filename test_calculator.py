from SolveEquation import solve_equation

def test_calculator():
    assert solve_equation("3+5") == 8
    assert solve_equation(" - 2 + 7 ") == 5
    assert solve_equation(" 0 + 0 ") == 0

    assert solve_equation(" 9 -4") == 5
    assert solve_equation("-5-(-3)") == -2
    assert solve_equation(" 0 - 8 ") == -8

    assert solve_equation(" 4 * 7") == 28
    assert solve_equation(" - 3 * 6") == - 18
    assert solve_equation("0 * 5") == 0

    assert solve_equation("10/2") == 5
    assert solve_equation(" 9 / 4 ") == 2.25
    assert solve_equation(" -12 / 3 ") == -4
    print("Expected Error: division by zero")
    assert solve_equation(" 5 / 0") is None

    assert solve_equation("2^3") == 8
    assert solve_equation(" 5 ^ 0 ") == 1
    assert solve_equation("(-2)^4") == 16

    assert solve_equation("10%3") == 1
    assert solve_equation("-7 % 4") == -3
    assert solve_equation("5%5") == 0

    assert solve_equation("5$8") == 8
    assert solve_equation(" (-3) $ 2") == 2
    assert solve_equation("0$-1") == 0

    assert solve_equation("5&8") == 5
    assert solve_equation("2 & -3") == -3
    assert solve_equation(" - 1 & 0 ") == 0

    assert solve_equation("4@6") == 5
    assert solve_equation(" 10 @ -2 ") == 4
    assert solve_equation(" 0@0 ") == 0

    assert solve_equation("~5") == -5
    assert solve_equation(" ~ -3 ") == 3
    assert solve_equation(" ~ 0 ") == 0

    assert solve_equation("5!") == 120
    assert solve_equation(" 0 ! ") == 1
    assert solve_equation(" 3! ") == 6

    assert solve_equation("3#") == 3
    assert solve_equation(" 0 # ") == 0
    assert solve_equation(" 3.255# ") == 15

    assert solve_equation("3 + 5 * 2") == 13
    assert solve_equation("(10-2)^2/4") == 16
    assert solve_equation(" 5 ! + 3 ^ 2 ") == 129
    assert solve_equation(" ( 8 - 3 ) ^ 2 / 5") == 5
    assert solve_equation("4*(6+3)-2") == 34
    assert solve_equation("(10 % 3) + 4 $ 6") == 7
    assert solve_equation("8 $ (7 - 5) * 2") == 16
    print("Expected Error: negative factorial number")
    assert solve_equation("~(3 + 2)!") is None
    assert solve_equation("5! / (2 * 3)") == 20
    assert solve_equation("~4 + 3 ^ 2") == 5
    assert solve_equation("(3 + 5) * 2 ^ 3 - 4 / 2") == 62
    assert solve_equation("10 * (2 + 3) ^ 2 - 5!") == 130
    assert solve_equation("~(4 @ 8) + 6 $ 10") == 4
    assert solve_equation("(10 % 4) + 3 * (~2 ^ 2)") == 14
    assert solve_equation(" (5! + 3 ^ 2) % 4 ") == 1
    assert solve_equation("10 / 2 + 5 * (~3 $ 6)") == 35
    assert solve_equation("((3 + 5 * 2) ^ 2 % 7) * (4 - 6 / 2) + 5!") == 289
    assert solve_equation("((((3 ^ 2) * 4) - (8 / 2)) $ (10 % 4)) @ (~5 + 7)") == 17
    assert solve_equation(" ((5! - (3 * 4)) / ((8 ^ 2) % 7) ) +  ( (6 & 10) $ (2 * (4 - 3) ) ) ") == 114
    assert solve_equation(" ( ( (7! / (3 + 4)) % 5) ^ 2) + (~(6 $ 2) * (10 - ( 4 @ 8)) )") == -24
    assert solve_equation("(((((1)))))") == 1
    assert solve_equation("((3! + (5 * 2)) ^ 2 / (10 - 8)) + ((4! - 6) * (7 % 3)) - ((2 ^ 3) $ (8 @ 6))") == 138
    assert solve_equation("~(-5)! + 6") == 126
    print("Expected Error: tilda cant come after minus")
    assert solve_equation("-~3") is None
    print("Expected Error: tilda cant come after minus")
    assert solve_equation("1+-~3") is None
    assert solve_equation("------2") == 2
    print("Expected Error: tilda cant come after tilda")
    assert solve_equation("~~2") is None
    assert solve_equation("5") == 5
    assert solve_equation("(2)") == 2
    print("Expected Error: Expecting operand")
    assert solve_equation("") is None
    print("Expected Error: Expecting operand")
    assert solve_equation("\t2") == 2
    assert solve_equation("~(~5)") == 5
    print("Expected Error: Expecting operand")
    assert solve_equation(" - ") is None
    print("Expected Error: Expecting operator left")
    assert solve_equation("!") is None
    assert solve_equation("    \t                       \n\n  \n                    2                            \n\t\t\t\t\t\t") == 2
    assert solve_equation(" 1 " + (" + 1" * 1000)) == 1001
    print("Expected Error: Missing Operand")
    assert solve_equation("5 + ") is None
    print("Expected Error: Missing Operand")
    assert solve_equation(" * 3 ") is None
    print("Expected Error: Missing Operand")
    assert solve_equation("( 4 - ) ^ 2") is None
    print("Expected Error: Spaces between Operand")
    assert solve_equation("5 5") is None

