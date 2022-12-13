#!/usr/bin/env python3

import dataclasses
import math
import operator
import sys
import typing

Operator = typing.Union[operator.add, operator.sub, operator.mul, operator.truediv]


def get_operator_from_str(s: str) -> Operator:
    match s:
        case "+":
            return operator.add
        case "-":
            return operator.sub
        case "*":
            return operator.mul
        case "/":
            return operator.truediv
        case _:
            raise RuntimeError("impossible")


@dataclasses.dataclass
class Monkey:
    items_worry: list[int]
    calculate_worry: str
    test_throw_divisible: int
    test_throw_true_monkey_id: int
    test_throw_false_monkey_id: int
    items_inspected: int = dataclasses.field(default=0)
    calculate_worry_operator: Operator = dataclasses.field(init=False)
    calculate_worry_val1: int | None = dataclasses.field(init=False)
    calculate_worry_val2: int | None = dataclasses.field(init=False)

    def __post_init__(self) -> None:
        calculate_worry_split = self.calculate_worry.split(" ")

        operator_str = calculate_worry_split[1]
        self.calculate_worry_operator = get_operator_from_str(operator_str)

        self.calculate_worry_val1 = (
            None if calculate_worry_split[0] == "old" else int(calculate_worry_split[0])
        )
        self.calculate_worry_val2 = (
            None if calculate_worry_split[2] == "old" else int(calculate_worry_split[2])
        )

    def add_item(self, item_worry: int) -> None:
        self.items_worry.append(item_worry)

    def get_monkey_id_to_throw(self) -> int:
        if self.items_worry[0] % self.test_throw_divisible == 0:
            return self.test_throw_true_monkey_id
        return self.test_throw_false_monkey_id

    def throw_first_item_to(self, monkey: "Monkey") -> None:
        monkey.add_item(self.items_worry.pop(0))

    def update_first_item_new_worry(self) -> None:
        val1 = (
            self.items_worry[0]
            if self.calculate_worry_val1 is None
            else self.calculate_worry_val1
        )

        val2 = (
            self.items_worry[0]
            if self.calculate_worry_val2 is None
            else self.calculate_worry_val2
        )

        self.items_worry[0] = self.calculate_worry_operator(val1, val2)

        self.items_worry[0] = math.floor(self.items_worry[0] / 3)


items_inspected = {}
monkeys: dict[int, Monkey] = {}

reading_monkey_id = -1
reading_monkey_attrs = {}
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    elif line.startswith("Monkey "):
        reading_monkey_id = int(line.split(" ")[1].replace(":", ""))
        items_inspected[reading_monkey_id] = 0
        reading_monkey_attrs = {}
    elif line.startswith("Starting items:"):
        reading_monkey_attrs["items_worry"] = list(
            map(int, line.replace("Starting items: ", "").split(", "))
        )
    elif line.startswith("Operation: "):
        reading_monkey_attrs["calculate_worry"] = line.replace("Operation: new = ", "")
    elif line.startswith("Test:"):
        reading_monkey_attrs["test_throw_divisible"] = int(
            line.replace("Test: divisible by ", "")
        )
    elif line.startswith("If true:"):
        reading_monkey_attrs["test_throw_true_monkey_id"] = int(
            line.replace("If true: throw to monkey ", "")
        )
    elif line.startswith("If false:"):
        reading_monkey_attrs["test_throw_false_monkey_id"] = int(
            line.replace("If false: throw to monkey ", "")
        )

        monkeys[reading_monkey_id] = Monkey(**reading_monkey_attrs)
        reading_monkey_id = -1
        reading_monkey_attrs = {}


for _ in range(20):
    for monkey_idx, monkey_obj in monkeys.items():
        nb_items_monkey = len(monkey_obj.items_worry)
        for _ in range(nb_items_monkey):
            monkey_obj.update_first_item_new_worry()
            items_inspected[monkey_idx] += 1

            monkey_obj_to_throw = monkeys[monkey_obj.get_monkey_id_to_throw()]
            monkey_obj.throw_first_item_to(monkey_obj_to_throw)

items_inspected = list(items_inspected.values())

max1 = max(items_inspected)
items_inspected.remove(max1)
max2 = max(items_inspected)

print(max1 * max2)
