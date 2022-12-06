# prompt: https://adventofcode.com/2022/day/6

# from typing import Tuple
from ...base import TextSolution, answer
from collections import deque


class Solution(TextSolution):
    _year = 2022
    _day = 6

    @answer(1929)
    def part_1(self) -> int:
        signal = self.input
        marker_length: int = 4
        markers = deque(maxlen=marker_length)
        for idx, char in enumerate(signal, start=1):
            markers.append(char)
            if len({*markers}) == marker_length:
                return idx

    @answer(3298)
    def part_2(self) -> int:
        signal = self.input
        marker_length: int = 14
        markers = deque(maxlen=marker_length)
        for idx, char in enumerate(signal, start=1):
            markers.append(char)
            if len({*markers}) == marker_length:
                return idx

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
