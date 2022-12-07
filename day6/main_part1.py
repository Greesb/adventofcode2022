#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    buffer = sys.stdin.readline().strip()
    i = 0
    while i < len(buffer) - 4:
        if len(set(buffer[i : i + 4])) == 4:
            print(i + 4)
            break

        i += 1
