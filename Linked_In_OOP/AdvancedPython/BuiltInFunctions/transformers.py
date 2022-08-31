# use transform functions like sorted, filter, map


def filterFunc(x):
    if x % 2 == 0:
        return False
    return True


def filterFunc2(x):
    if x.isupper():
        return False
    return True


def squareFunc(x):
    return x**2


def toGrade(x):
    if (x >= 90):
        return "A"
    elif (x >=80 and x < 90):
        return "B"
    elif (x >=70 and x < 80):
        return "C"
    elif (x >=60 and x < 70):
        return "D"
    return "F"


def main():
    # define some sample sequences to operate on
    nums = (1, 2, 8, 4, 13, 26, 381, 410, 58, 47)
    chars = "abcdefghiJkLmnOP"
    grades = (81, 89, 94, 71, 66, 99, 73, 42)

    # TODO: use filter to remove items from a list
    odds = list(filter(filterFunc, nums))
    print(odds)

    # TODO: use filter non-numeric sequence
    lowers = list(filter(filterFunc2, chars))
    print(lowers)

    # TODO: use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(squares)

    # TODO: use sort and map to change numbers to grades
    grades = sorted(grades)
    letter_grades = list(map(toGrade, grades))
    print(letter_grades)


if __name__ =="__main__":
    main()