#!/usr/bin/env python3

import math
import sys
import typing

MoveT = typing.Literal["L", "R", "U", "D"]
PositionT = tuple[int, int]


def get_positions_distance(p1: PositionT, p2: PositionT) -> float:
    return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))


def are_positions_touching(head: PositionT, tail: PositionT) -> bool:
    return get_positions_distance(head, tail) < 2


def move_position(position: PositionT, move: MoveT) -> PositionT:
    match move:
        case "L":
            return (position[0], position[1] - 1)
        case "R":
            return (position[0], position[1] + 1)
        case "U":
            return (position[0] - 1, position[1])
        case "D":
            return (position[0] + 1, position[1])
        case _:
            raise RuntimeError(f"Unrecognized move {move}")


visited = set([0])
head_pos = (0, 0)
tail_pos = (0, 0)

for line in sys.stdin:
    move, nb = line.strip().split(" ")
    for _ in range(int(nb)):
        prev_head_pos = head_pos
        head_pos = move_position(head_pos, move)
        if not are_positions_touching(head_pos, tail_pos):
            tail_pos = prev_head_pos
            visited.add(tail_pos)


print(len(visited))
