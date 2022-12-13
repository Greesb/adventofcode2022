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
            return (position[0] + 1, position[1])
        case "D":
            return (position[0] - 1, position[1])
        case _:
            raise RuntimeError(f"Unrecognized move {move}")


def get_movement(prev_pos: PositionT, pos_to_check: PositionT) -> MoveT:
    s = ""
    if prev_pos[0] != pos_to_check[0]:
        s += "U" if prev_pos[0] > pos_to_check[0] else "D"
    if prev_pos[1] != pos_to_check[1]:
        s += "R" if prev_pos[1] > pos_to_check[1] else "L"
    return s


def multiple_moves(position: PositionT, moves: list[MoveT]) -> PositionT:
    for m in moves:
        position = move_position(position, m)
    return position


visited = set([0])
head_pos = (0, 0)
tails_pos = [(0, 0)] * 9

for line in sys.stdin:
    move, nb = line.strip().split(" ")
    for j in range(int(nb)):
        prev_pos = head_pos
        head_pos = move_position(head_pos, move)
        tail_pos_check = head_pos
        for i in range(0, 9):
            if are_positions_touching(tail_pos_check, tails_pos[i]):
                break

            dist = get_positions_distance(tail_pos_check, tails_pos[i])
            if i == 0 or dist < 2:
                tails_pos[i], prev_pos = prev_pos, tails_pos[i]
            else:
                movements = get_movement(tail_pos_check, tails_pos[i])
                prev_pos = tails_pos[i]
                tails_pos[i] = multiple_moves(tails_pos[i], movements)

            tail_pos_check = tails_pos[i]

            if i == 8:
                visited.add(tails_pos[8])


print(len(visited))
