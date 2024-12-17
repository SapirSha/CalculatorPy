from SolveEquation import solve_equation


def main():
    res = solve_equation("-3 \t")

    if res is not None:
        print(res)

if __name__ == "__main__":
    main()