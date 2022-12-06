# prompt: https://adventofcode.com/2022/day/3

# from typing import Tuple
from typing import List, Tuple
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 3

    @answer(7817)
    def part_1(self) -> int:
        rucksacks = self.input

        strings = "abcdefghijklmnopqrstuvwxyz"
        strings = strings + strings.upper()

        def divide_rucksacks(rucksack: str) -> Tuple[str, str]:
            half = int(len(rucksack) / 2)
            return rucksack[:half], rucksack[half:]

        def check_duplicates(compartment_1: str, compartment_2: str) -> str:
            for item in compartment_1:
                if item in [*compartment_2]:
                    return item

        priorities = 0
        for rucksack in rucksacks:
            i = check_duplicates(*divide_rucksacks(rucksack))
            priorities += strings.index(i) + 1

        return priorities

    @answer(2444)
    def part_2(self) -> int:
        rucksacks = self.input

        strings = "abcdefghijklmnopqrstuvwxyz"
        strings = strings + strings.upper()

        def make_group(all_rucksacks: list) -> List[Tuple[str, str, str]]:
            groups = []
            for pos in range(0, len(all_rucksacks), 3):
                group = (*all_rucksacks[pos : pos + 3],)
                groups.append(group)
            return groups

        def check_commons(elf_1: str, elf_2: str, elf_3: str) -> str:
            for item in elf_1:
                if item in [*elf_2]:
                    if item in [*elf_3]:
                        return item

        priorities = 0
        for group in make_group(rucksacks):
            i = check_commons(*group)
            priorities += strings.index(i) + 1

        return priorities

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
