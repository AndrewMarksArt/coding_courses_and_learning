# examples of comprehensions (lists, dict, sets, etc.)
# [ "output" "the vars working on" "where the vars come from"]
# example: FarenheitToCelsius
# [ (t*9/5) for t in [32, 65, 104, 212] ]


def main():
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: perform a mapping and filter funcs
    # square elements in evens if grater then 4 but less than 16
    evenSquare = list(
        map(lambda e: e**2, filter(lambda e: e>4 and e<16, evens)))
    print(evenSquare)

    # TODO: use list comprhension
    evenSquared = [ e**2 for e in evens]
    print(evenSquared)

    oddsSquared = [e**2 for e in odds if e > 3 and e < 17]
    print(oddsSquared)


if __name__ == "__main__":
    main()
