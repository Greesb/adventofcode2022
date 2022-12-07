#!/usr/bin/env python3
import re
import sys

columns = {}
moving = False

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if len(line.strip()) == 0:
            moving = True
            print(columns)
            continue

        if not moving:
            if line[0] == " ":
                continue

            cols = 1
            idx = 0
            while idx < len(line):
                if cols not in columns:
                    columns[cols] = []
                if line[idx] == "[":
                    columns[cols].append(line[idx + 1])
                idx += 4
                cols += 1

        if moving:
            m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            nb_move = int(m.group(1))
            from_move = int(m.group(2))
            to_move = int(m.group(3))

            to_insert = columns[from_move][:nb_move].copy()
            to_insert.reverse()
            columns[to_move][:0] = to_insert

            columns[from_move] = columns[from_move][nb_move:]

res = ""
for n in columns:
    if len(columns[n]):
        res += columns[n][0]

print(res)
