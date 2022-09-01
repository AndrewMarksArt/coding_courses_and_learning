# deonstrate ordered dictionaries

from collections import OrderedDict


def main():
    # sports teams with wins and loses
    teams = [
        ("Dodgers", (88, 53)),
        ("Yankees", (76, 63)),
        ("Kings", (15, 15)),
        ("Jets", (8, 8)),
        ("Dragons", (22, 8))
    ]

    # sort teams by number of wins
    by_wins = sorted(teams, key=lambda t: t[1][0], reverse=True)
    print(by_wins)

    # TODO: create ordered dict
    teams_dict = OrderedDict(teams)
    print(teams_dict)

    # TODO: use popitem to remove top team
    tm, wl = teams_dict.popitem(False)
    print("Top team: ", tm, wl)

    # TODO: what are the next 4 teams
    for i, team in enumerate(teams_dict, start=1):
        print(i, team)
        if i == 4:
            break

    # TODO test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})
    print("equality test: ", a == b)

    # comparing ordered to ordered --> order matters
    c = OrderedDict({"a": 1, "c": 3, "b": 2})
    print("equality test: ", a == c)

    # comparing ordered to reg dict --> order doesnt matter
    d = {"a": 1, "c": 3, "b": 2}
    print("equality test: ", a == d)


if __name__ == "__main__":
    main()
