
from SolveEquation import solve_equation


def main():
    res = solve_equation("(100 + 250 + 300 + 400 * -2)-~-3")

    if res is not None:
        print(res)

if __name__ == "__main__":
    main()