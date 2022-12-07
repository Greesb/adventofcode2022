#!/usr/bin/env python3
import enum
import sys


class RockPaperScissor(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __gt__(self, other):
        # ROCK > SCISSORS
        if self.value == 1 and other.value == 3:
            return True
        elif self.value == 3 and other.value == 1:
            return False
        return self.value > other.value


CLASS_MAPPING: dict[str, RockPaperScissor] = {
    "A": RockPaperScissor.ROCK,
    "X": RockPaperScissor.ROCK,
    "B": RockPaperScissor.PAPER,
    "Y": RockPaperScissor.PAPER,
    "C": RockPaperScissor.SCISSORS,
    "Z": RockPaperScissor.SCISSORS,
}

score = 0
for line in sys.stdin:
    opponent, me = [CLASS_MAPPING[v] for v in line.strip().split(" ")]
    score += me.value
    if opponent == me:
        score += 3
    elif me > opponent:
        score += 6


print(score)
