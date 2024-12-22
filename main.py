from SolveEquation import solve_equation

def ui_sort_of():
    try:
        inp = input(" - Enter Equation (stop to stop): ")
        if inp.strip().lower() == "stop":
            raise KeyboardInterrupt

        res =  solve_equation(inp)

        return res
    except UnicodeError:
        print("<--- Error ------------------------------>")
        print("Error decoding input!")
        print("<---------------------------------------->")
        return
    except EOFError:
        raise KeyboardInterrupt
    except MemoryError:
        print("<--- Error ------------------------------>")
        print("Equation too big!")
        print("<---------------------------------------->")
        return
    # just forget about all the exceptions raised in solve equation
    except Exception:
        return


def main():
    print("\t--- Start Program --- \n")

    try:
        while True:
            res = ui_sort_of()
            if res is not None:
                try:
                    print(f"Answer: {res}")
                except ValueError:
                    print("<--- Error ------------------------------>")
                    print("Value too big to print")
                    print("<---------------------------------------->")
    except KeyboardInterrupt:
        pass

    print("\n\t--- Program End ---")


if __name__ == "__main__":
    main()
