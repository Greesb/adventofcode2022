#!/usr/bin/env python3

import sys

X = 1
cycle = 1


def print_X(cycle: int) -> None:
    if X - 1 <= (cycle - 1) % 40 <= X + 1:
        print("#", end="")
    else:
        print(".", end="")

    if cycle % 40 == 0:
        print("")


for line in sys.stdin:
    l = line.strip().split(" ")

    print_X(cycle)

    if l[0] == "noop":
        pass
    elif l[0] == "addx":
        cycle += 1
        print_X(cycle)

        X += int(l[1])

    cycle += 1
