# use iterator functions like enumerate, zip, iter, next

def main():
    # define a list of days in English and French
    days = ["sun", "mon", "tue", "wed", "thur", "fri", "sat"]
    daysFr = ["dim", "lun", "mar", "mer", "jeu", "ven", "sam"]

    # TODO: use iter to create an iterator over a collection
    """ i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i)) """

    # TODO: iterate using a function and a sentinel
    """ with open("textfile.txt", "r") as fp:
        for line in iter(fp.readline, ''):
            print(line) """

    # TODO: use regular iteration over days
    # very easy to get too complex and could just use enumerate
    """ for m in range(len(days)):
        print(m+1, days[m]) """

    # much better way
    """ for i,m in enumerate(days, start=1):
        print(i, m) """

    # TODO: using enumerate reduces code and provides a conuter
    for i,m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")

    # TODO: use zip to combine sequences
    for m in zip(days, daysFr):
        print(m)

    # if two sequences arent the same length, zip terminates when the shorter one finishes


if __name__ == "__main__":
    main()
