from SolveEquation import solve_equation
from pytest import raises
from SolveTree.CalculationError import CalculationError


def test_calculator():
    with raises(SyntaxError):
        solve_equation("       ")
    with raises(SyntaxError):
        solve_equation("      \t\n\t ")

    with raises(SyntaxError):
        solve_equation("AWASDWASD")

    assert solve_equation("3+5") == 8
    assert solve_equation(" - 2 + 7 ") == 5
    assert solve_equation(" 0 + 0 ") == 0

    assert solve_equation(" 9 -4") == 5
    assert solve_equation("-5-(-3)") == -2
    assert solve_equation(" 0 - 8 ") == -8

    assert solve_equation(" 4 * 7") == 28
    assert solve_equation(" - 3 * 6") == -18
    assert solve_equation("0 * 5") == 0

    assert solve_equation("10/2") == 5
    assert solve_equation(" 9 / 4 ") == 2.25
    assert solve_equation(" -12 / 3 ") == -4
    with raises(CalculationError):
        solve_equation(" 5 / 0")

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
    with raises(CalculationError):
        solve_equation("~(3 + 2)!")
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
    with raises(SyntaxError):
        solve_equation("-~3")
    with raises(SyntaxError):
        solve_equation("1+-~3")
    assert solve_equation("------2") == 2
    with raises(SyntaxError):
        solve_equation("~~2")
    assert solve_equation("5") == 5
    assert solve_equation("(2)") == 2
    with raises(SyntaxError):
        solve_equation("")
    assert solve_equation("\t2") == 2
    assert solve_equation("~(~5)") == 5
    with raises(SyntaxError):
        solve_equation(" - ")
    with raises(SyntaxError):
        solve_equation("!")
    assert solve_equation(
        "    \t                       \n\n  \n                    2                            \n\t\t\t\t\t\t") == 2
    assert solve_equation(" 1 " + (" + 1" * 1000)) == 1001
    with raises(SyntaxError):
        assert solve_equation("5 + ") is None
    with raises(SyntaxError):
        solve_equation(" * 3 ")
    with raises(SyntaxError):
        solve_equation("( 4 - ) ^ 2")
    with raises(SyntaxError):
        assert solve_equation("5 5")
    with raises(SyntaxError):
        solve_equation("(5 + (3 - 2)")
    with raises(SyntaxError):
        solve_equation("5 + 3)")
    with raises(SyntaxError):
        solve_equation("10 ^ 2 $ 4 @ a")
    with raises(SyntaxError):
        solve_equation("5 ^ ^ 2")
    with raises(SyntaxError):
        solve_equation("5.5.3 + 2")

    assert solve_equation("((((((((((((5 @ 3))))))))))))") == 4
    assert solve_equation("123#") == 6
    assert solve_equation(".123#") == 6
    assert solve_equation("-123#") == -6
    assert solve_equation("100 *20 # ") == 200
    assert solve_equation("((5!)#)#") == 3
    with raises(CalculationError):
        solve_equation("((4 + 6)# - 5.5)#")

    assert solve_equation("(123# * (45 + 67)#) / (10# + 1)") == 12
    assert solve_equation("((5! + 200)# * (99#)) / ((10 + 45)# ^ 2)") == 0.9
    assert solve_equation("(5 * 4# + (123 ^ 2)#) / (50#)") == 7.6

    assert round(solve_equation("(((12! % 45) + (67 $ 89)) ^ 2) / (10 & 5) * (12 - 3)"), 5) == 14257.8
    assert solve_equation("(8 * (3! + 45)) @ ((4 ^ 2) - (7! / (3 + 2)))") == -292
    assert solve_equation("((5 $ 10) ^ 3) - ((2! + 7) * (45 @ 6))") == 770.5
    assert solve_equation("((((5! / 2) ^ 3) + 100) * (12 @ 4)) / 3") == 576266.6666666666666666666666
    assert solve_equation("(123# * (456 $ 789) ^ 2) - ((8! / 4) @ 56)") == 3730058
    assert solve_equation("(((3! * 4!) ^ 2) / (5 @ 3)) + ((10 % 2) $ 1)") == 5185
    assert solve_equation("45! / 10# + 20 @ 3 - 9 $ 7 ^ 2") == 1.1962222086548019e+56
    assert solve_equation("123! % 555.5 $ (7 ^ 3) + 8! / 4 @ 2") == 13880
    assert solve_equation("(((9 & 7) ^ 2) + (((4! - 2) / 3)) - ((12 $ (5))))") == 44.3333333333333333333333333
    assert solve_equation("(((3 + 5 ^ 2) @ 10) - ((9! / 6) $ 8))") == -60461
    assert solve_equation("5 + ~-3 + 2 * .33333333333333333333333333333 * (3/1) ") == 10
    assert solve_equation("-222^2 + -222^2 + .12345# + 12345.12345# + 12345.0# ") == 60
    assert solve_equation("(8 * 9 ^ 3 + 45 / 6 @ 2) ^ 2") == 34143570.5625
    assert solve_equation(" ( ( 3 ! + 5 ) @ ( 7 ^ 2 ) ) * ( ( 8 / 4 ) $ 9 ) ") == 270
    assert solve_equation("(((3^2)*5)-((7&6)/2))+(12!%4)") == 42
    assert solve_equation("(((10 @ 5!) % 4) + ((3 $ 7) / 8)) ^ 2") == 3.515625
    assert solve_equation("(((45 * 2!) @ 10) - ((9 $ 8) % 3)) * (4! + 3)") == 1350
    with raises(CalculationError):
        solve_equation("((123! + (45 @ 6)) ^ 2) - ((8 $ 7) / 4)")
    assert solve_equation("(((3! / 2) @ (4 $ 5)) + ((9 & 8) ^ 3))") == 516

    assert solve_equation("-.1234") == -0.1234
    with raises(SyntaxError):
        solve_equation("1+-~-44")
    with raises(SyntaxError):
        solve_equation("-~-44")
    assert solve_equation("1-~44") == 45
    assert solve_equation("-(~-44)") == -44
    with raises(SyntaxError):
        solve_equation("~~3")
    assert solve_equation("-5!") == -120
    with raises(CalculationError):
        solve_equation("~5!")
    with raises(CalculationError):
        solve_equation("~123#")
    assert solve_equation("-123#") == -6

    assert solve_equation("2.3#") == 5
    assert solve_equation("99##") == 9
