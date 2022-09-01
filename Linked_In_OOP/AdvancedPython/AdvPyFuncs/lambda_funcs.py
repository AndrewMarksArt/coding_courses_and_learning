#  - small anonymous functions
#  - can be passed as arguments to another function
#  - typically used in place just when needed to not add complexity
#    or reduce readability
# - Defined as --> lambda (parameters) : (expression)


def C_to_F(temp):
    return (temp * 9/5) + 32


def F_to_C(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # TODO: use regular functions to convert
    print(list(map(F_to_C, ftemps)))
    print(list(map(C_to_F, ctemps)))

    # TODO: use lambdas to convert
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    print(list(map(lambda t: (t*9/5) + 32, ctemps)))


if __name__ == "__main__":
    main()
