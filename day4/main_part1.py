#!/usr/bin/env python3

import sys

count = 0
if __name__ == "__main__":
    for line in sys.stdin:
        elf1, elf2 = line.strip().split(",")
        elf1_set = set(range(int(elf1.split("-")[0]), int(elf1.split("-")[1]) + 1))
        elf2_set = set(range(int(elf2.split("-")[0]), int(elf2.split("-")[1]) + 1))
        elf_union = elf1_set | elf2_set

        if elf_union == elf1_set or elf_union == elf2_set:
            count += 1

print(count)
