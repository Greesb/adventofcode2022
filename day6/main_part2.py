#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    buffer = sys.stdin.readline().strip()
    i = 0
    while i < len(buffer) - 14:
        if len(set(buffer[i : i + 14])) == 14:
            print(i + 14)
            break

        i += 1
