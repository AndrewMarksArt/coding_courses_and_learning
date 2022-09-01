#  demonstrate the usage of default dict objects

from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dict to count wach element
    fruitCount = {}

    for fruit in fruits:
        if fruit in fruitCount.keys():
            fruitCount[fruit] += 1
        else:
            fruitCount[fruit] = 1

    # redo with default dict
    fCount = defaultdict(int)
    for fruit in fruits:
        fCount[fruit] += 1

    for (k, v) in fruitCount.items():
        print(k + ": " + str(v))

    for (k, v) in fCount.items():
        print(k + ": " + str(v))


if __name__ == "__main__":
    main()
