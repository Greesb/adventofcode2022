#!/usr/bin/env python3

import math
import sys

_map = []
start = None
end = None


PositionT = tuple[int, int]


def get_positions_distance(p1: PositionT, p2: PositionT) -> float:
    return math.sqrt(pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2))


def successors(node: PositionT, _map: list[str]) -> list[PositionT]:
    relative_pos_to_try = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    successors = []
    for relative_pos in relative_pos_to_try:
        new_pos = (node[0] + relative_pos[0], node[1] + relative_pos[1])
        if (
            len(_map) > new_pos[0] >= 0
            and len(_map[0]) > new_pos[1] >= 0
            and (
                ord(_map[node[0]][node[1]]) >= ord(_map[new_pos[0]][new_pos[1]])
                or ord(_map[node[0]][node[1]]) + 1 == ord(_map[new_pos[0]][new_pos[1]])
            )
        ):
            successors.append(new_pos)

    return successors


def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.insert(0, current)
    print(len(total_path) - 1)
    return total_path


# // A* finds a path from start to goal.
# // h is the heuristic function. h(n) estimates the cost to reach goal from node n.
def a_star(start, goal):
    # // The set of discovered nodes that may need to be (re-)expanded.
    # // Initially, only the start node is known.
    # // This is usually implemented as a min-heap or priority queue rather than a hash-set.
    openSet = {start}

    # // For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start
    # // to n currently known.
    cameFrom = {}

    # // For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = {}
    gScore[start] = 0

    # // For node n, fScore[n] := gScore[n] + h(n). fScore[n] represents our current best guess as to
    # // how cheap a path could be from start to finish if it goes through n.
    fScore = {}
    fScore[start] = 0

    while openSet:
        # // This operation can occur in O(Log(N)) time if openSet is a min-heap or a priority queue
        min_val = (sys.maxsize, None)
        for node in openSet:
            if fScore[node] < min_val[0]:
                min_val = (fScore[node], node)

        # current := the node in openSet having the lowest fScore[] value
        current = min_val[1]
        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        for neighbor in successors(current, _map):
            # // d(current,neighbor) is the weight of the edge from current to neighbor
            # // tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + 1
            if tentative_gScore < gScore.get(neighbor, sys.maxsize):
                # // This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + gScore[current] + 1
                if neighbor not in openSet:
                    openSet.add(neighbor)

    # // Open set is empty but goal was never reached
    return None


for line in sys.stdin.readlines():
    _map.append(line.strip())

    if "E" in line:
        end = (len(_map) - 1, line.index("E"))
        _map[-1] = _map[-1].replace("E", "z")
    if "S" in line:
        start = (len(_map) - 1, line.index("S"))
        _map[-1] = _map[-1].replace("S", "a")


a_star(start, end)
