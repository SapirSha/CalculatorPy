from SolveEquation import solve_equation


def ui_sort_of():
    try:
        inp = input(" - Enter Equation (stop to stop): ")
        if inp.strip().lower() == "stop":
            raise KeyboardInterrupt

        return solve_equation(inp)
    except Exception:
        return


def main():
    print("\t--- Start Program --- \n")

    try:
        while True:
            res = ui_sort_of()
            if res is not None:
                print(f"Answer: {res}")
    except KeyboardInterrupt:
        pass

    print("\n\t--- Program End ---")


if __name__ == "__main__":
    main()
