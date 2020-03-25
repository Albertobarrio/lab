#!/usr/bin/python3
import sys

number = sys.argv[1]


def add(number):
    result = 0
    for i in range(1, 4):
        result += int(number*i)
    print(result)


if __name__ == "__main__":
    add(number)
