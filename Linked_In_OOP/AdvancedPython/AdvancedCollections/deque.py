# Demonstrate Deque
# Double-ended queue, pronounced "deck"
# append or pop data from either side and memory efficent
# d = collections.deque('abcde)
# appendleft() to add to the front and append() for end
# popleft() to pop first and pop() to pop last
# rotate() provide how many elements to move to front or back

import collections
import string


def main():
    # TODO: init deque with lower case letter
    d = collections.deque(string.ascii_lowercase)

    # TODO: deques support len()
    print("Item count: ", str(len(d)))

    # TODO: loop over and make upper
    # for ele in d:
    #    print(ele.upper(), end=",")

    # TODO: manipulate items
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    # print(d)

    # TODO: rotate
    print(d)
    d.rotate(10)
    print(d)


if __name__ == "__main__":
    main()
