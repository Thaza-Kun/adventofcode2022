# prompt: https://adventofcode.com/2022/day/9

# from typing import Tuple
from collections import defaultdict
from copy import deepcopy
from typing import Dict, List, Tuple, Union
from ...base import StrSplitSolution, TextSolution, answer
from pprint import pprint


Coords = Tuple[int, int]


class Rope:
    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]
        self.visited_by_tail = {(*self.tail,)}

    @property
    def length(self) -> Tuple[int, int]:
        dx = self.head[0] - self.tail[0]
        dy = self.head[1] - self.tail[1]
        return dx, dy

    def move_head(self, movement: Tuple[Coords, int]) -> None:
        (dx, dy), distance = movement
        for _ in range(distance):
            self.head[0] += dx
            self.head[1] += dy
            self.update_tail()
            self.visited_by_tail.add((*self.tail,))

    def update_tail(self) -> None:
        dx, dy = self.length
        if dx < 0:
            x_sign = -1
        else:
            x_sign = 1
        if dy < 0:
            y_sign = -1
        else:
            y_sign = 1
        if (dx + dy == 1 or dx + dy == 0) and (abs(dx) == 1 and abs(dy) == 1):
            return
        if self.head != self.tail:
            if dy == 0:
                self.tail[0] += dx - x_sign * 1
            elif dx == 0:
                self.tail[1] += dy - y_sign * 1
            elif abs(dx) == 1 and abs(dy) != 1:
                self.tail = [self.tail[0] + dx, self.tail[1] + dy - y_sign * 1]
            elif abs(dx) != 1 and abs(dy) == 1:
                self.tail = [self.tail[0] + dx - x_sign * 1, self.tail[1] + dy]
            else:
                self.tail = [
                    self.tail[0] + dx - x_sign * 1,
                    self.tail[1] + dy - y_sign * 1,
                ]


directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


class Solution(StrSplitSolution):
    _year = 2022
    _day = 9

    @answer(6087)
    def part_1(self) -> int:
        rope = Rope()
        movements: List[str] = self.input

        for move in movements:
            components, distance = move.split()
            (dx, dy) = directions[move[0]]
            rope.move_head(((dx, dy), int(distance)))

        return len(rope.visited_by_tail)

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
