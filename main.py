from SolveEquation import solve_equation


def main():
    print("\t--- Start Program --- \n")
    print(solve_equation("123.12345*3"))
    '''
    try:
        while True:
            inp = input(" - Enter Equation: ")
            res = solve_equation(inp)

            if res is not None:
                print("Answer: ", end="")
                print(res)
    except KeyboardInterrupt:
        pass
        '''
    print("\n\t--- Program End ---")

if __name__ == "__main__":
    main()