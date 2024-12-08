from math import inf

from sortedcontainers import SortedList


def test():
    num = inf
    list = SortedList((-inf, inf))
    print(num)
    list.add(1)
    print(list)

if __name__ == "__main__":
    test()
