# Demonstrate the use of variable argument lists
# great way to add flexibility but need to becareful and think ahead
# if we make changes to the function by adding new parameters,
# we will need to go and make sure we update all of our function calls

# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    # TODO: pass different args
    print(addition(5, 10, 15, 20))
    print(addition(1, 2, 3))

    # TODO: pass an existing list
    my_nums = [5, 10, 15, 20]
    print(addition(*my_nums))


if __name__ == "__main__":
    main()
