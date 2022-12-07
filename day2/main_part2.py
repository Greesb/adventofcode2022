#!/usr/bin/env python3
import enum
import sys


class RockPaperScissor(enum.Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def get_winner_over_me(self) -> "RockPaperScissor":
        if self.value < 3:
            return RockPaperScissor(self.value + 1)
        return RockPaperScissor.ROCK

    def get_looser_from_me(self) -> "RockPaperScissor":
        if self.value > 1:
            return RockPaperScissor(self.value - 1)
        return RockPaperScissor.SCISSORS


CLASS_MAPPING: dict[str, RockPaperScissor] = {
    "A": RockPaperScissor.ROCK,
    "B": RockPaperScissor.PAPER,
    "C": RockPaperScissor.SCISSORS,
}

score = 0
for line in sys.stdin:
    opponent, turn_result = line.strip().split(" ")
    opponent = CLASS_MAPPING[opponent]

    if turn_result == "X":
        # LOOSE
        score += opponent.get_looser_from_me().value
    elif turn_result == "Y":
        # DRAW
        score += opponent.value + 3
    elif turn_result == "Z":
        # WIN
        score += opponent.get_winner_over_me().value + 6


print(score)
