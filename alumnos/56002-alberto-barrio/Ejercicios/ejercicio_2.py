#!/usr/bin/python3
import sys

number = sys.argv[1]
sums = int(sys.argv[2])


def add(number, sums):
    result = 0
    for i in range(1, sums+1):
        result += int(number*i)
    print(result)


if __name__ == "__main__":
    add(number, sums)
