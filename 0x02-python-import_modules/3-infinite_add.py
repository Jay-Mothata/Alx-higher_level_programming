#!/usr/bin/python3
import sys

if __name__ == "__main__":

    argv_count = len(sys.argv) - 1  # Subtract 1 for the script name
    index = 1
    res = 0

    while index <= argv_count:
        res += int(sys.argv[index])
        index += 1

        print("{}".format(res))
