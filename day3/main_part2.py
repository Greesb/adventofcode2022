#!/usr/bin/env python3
import sys

sum_ = 0
group_nb = 0
group = []

for line in sys.stdin:
    group.append(line.strip())
    group_nb += 1

    if group_nb > 2:
        doublon = set(group[0]) & set(group[1]) & set(group[2])
        doublon = doublon.pop()
        if ord(doublon) > 96:
            sum_ += ord(doublon) - 96
        else:
            sum_ += ord(doublon) - 38

        group_nb = 0
        group.clear()

print(sum_)
