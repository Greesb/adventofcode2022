#!/usr/bin/env python3
import sys

elves_calories = [0]
idx = 0

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            idx += 1
            elves_calories.append(0)
        else:
            elves_calories[idx] += int(line)


print(max(elves_calories))
