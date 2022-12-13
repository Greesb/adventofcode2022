#!/usr/bin/env python3

import sys

X = 1
_sum = 0
cycle = 1

for line in sys.stdin:
    if cycle in (20, 60, 100, 140, 180, 220):
        _sum += cycle * X

    l = line.strip().split(" ")
    if l[0] == "noop":
        pass
    elif l[0] == "addx":
        cycle += 1
        if cycle in (20, 60, 100, 140, 180, 220):
            _sum += cycle * X

        X += int(l[1])

    cycle += 1

print(_sum)
