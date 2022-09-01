# advanced iteration functions in the itertools package

import itertools


def testFunc(x):
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    """ seq1 = ["joe", "john", "mike", "andrew"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1)) """

    # TODO: use count to create a simple counter
    """ count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1)) """

    # TODO: accumulate creates an iterator that accumulates values
    """ vals = [10, 20, 30, 40, 50, 40, 30]
    # running count
    acc = itertools.accumulate(vals)
    print(list(acc))
    # pin max value
    acc = itertools.accumulate(vals, max)
    print(list(acc)) """

    # TODO: use chain to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))

    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    vals = [10, 20, 30, 40, 50, 40, 30]
    print(list(itertools.dropwhile(testFunc, vals)))
    print(list(itertools.takewhile(testFunc, vals)))


if __name__ == "__main__":
    main()