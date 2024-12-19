from SolveEquation import solve_equation
from Operators.Plus import Plus


def main():
    print("\t--- Start Program --- \n")
    inp = ""

    try:
        while True:
            inp = input(" - Enter Equation (stop to stop): ")
            if inp.strip().lower() == "stop":
                break

            res = solve_equation(inp)

            if res is not None:
                print("Answer: ", end="")
                print(res)
    except KeyboardInterrupt:
        pass


    print("\n\t--- Program End ---")

if __name__ == "__main__":
    main()