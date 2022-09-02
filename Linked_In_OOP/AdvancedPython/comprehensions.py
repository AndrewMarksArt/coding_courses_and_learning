# examples of comprehensions (lists, dict, sets, etc.)
# [ "output" "the vars working on" "where the vars come from"]
# example: FarenheitToCelsius
# [ (t*9/5) for t in [32, 65, 104, 212] ]


def main():
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # dict comprehensions
    ctemps = [0, 12, 34, 100]
    tempDict = {t: (t*9/5) + 32 for t in ctemps if t < 100}
    print(tempDict)
    print(tempDict[12])

    # merge 2 dicts with comprehension
    t1 = {"jones": 24, "jameson": 18, "smith": 58, "burns": 7}
    t2 = {"white": 12, "macke": 88, "perce": 4}

    newTeam = {k:v for team in (t1, t2) for k,v in team.items()}
    print(newTeam)

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
