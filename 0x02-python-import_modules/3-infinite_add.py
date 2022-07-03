#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    tot = 0

    if len(argv) > 1:
        for i in range(1, len(argv)):
            tot += int(argv[i])
    print("{:d}".format(tot))
