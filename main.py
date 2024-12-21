from MakeTree.MakeTree import parentheses_stack
from SolveEquation import solve_equation

def ui_sort_of():
    try:
        inp = input(" - Enter Equation (stop to stop): ")
        if inp.strip().lower() == "stop":
            raise KeyboardInterrupt

        res =  solve_equation(inp)

        return res
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
