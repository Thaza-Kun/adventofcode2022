# prompt: https://adventofcode.com/2022/day/4

# from typing import Tuple
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 4

    @answer(534)
    def part_1(self) -> int:
        assigments = [pair.split(",") for pair in self.input]

        def check_containment(container_1: str, container_2: str) -> bool:
            start_1, end_1 = container_1.split("-")
            start_2, end_2 = container_2.split("-")
            first_range = range(int(start_1), int(end_1) + 1)
            second_range = range(int(start_2), int(end_2) + 1)
            if len(first_range) > len(second_range):
                longer_range = first_range
                shorter_range = second_range
            else:
                longer_range = second_range
                shorter_range = first_range
            for section in shorter_range:
                if section not in longer_range:
                    return False
            return True

        # Check check_containment logic
        assert check_containment("1-10", "2-5") is True
        assert check_containment("2-5", "1-10") is True
        assert check_containment("1-3", "5-7") is False
        assert check_containment("5-7", "1-3") is False

        count = 0
        for elf1, elf2 in assigments:
            if check_containment(elf1, elf2):
                count += 1

        return count

    @answer(841)
    def part_2(self) -> int:
        assigments = [pair.split(",") for pair in self.input]

        def check_overlap(container_1: str, container_2: str) -> bool:
            start_1, end_1 = container_1.split("-")
            start_2, end_2 = container_2.split("-")
            first_range = range(int(start_1), int(end_1) + 1)
            second_range = range(int(start_2), int(end_2) + 1)
            for i in first_range:
                if i in second_range:
                    return True
            return False

        count = 0
        for elf1, elf2 in assigments:
            if check_overlap(elf1, elf2):
                count += 1
        return count

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
