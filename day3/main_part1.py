#!/usr/bin/env python3
import sys

sum_ = 0
for line in sys.stdin:
    line_strip = line.strip()
    half_line_len = int(len(line_strip) / 2)
    line_first_half = line_strip[:half_line_len]
    line_second_half = line_strip[half_line_len:]

    set_1 = set(line_first_half)
    set_2 = set(line_second_half)
    for doublon in set_1 & set_2:
        if ord(doublon) > 96:
            sum_ += ord(doublon) - 96
        else:
            sum_ += ord(doublon) - 38


print(sum_)
