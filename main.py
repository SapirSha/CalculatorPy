from SolveEquation import solve_equation


def main():
    res = solve_equation("~0.5^0.5")

    if res is not None:
        print(res)

if __name__ == "__main__":
    main()