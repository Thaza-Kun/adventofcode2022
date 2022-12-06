# prompt: https://adventofcode.com/2022/day/1

# from typing import Tuple
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 1
    calories_per_elves = []

    @answer(72478)
    def part_1(self) -> int:
        foods = self.input
        food_per_elf = []
        for food in foods:
            if food == "":
                if len(food_per_elf) != 0:
                    self.calories_per_elves.append(sum(food_per_elf))
                food_per_elf = []
            else:
                food_per_elf.append(int(food))
        return max(self.calories_per_elves)

    @answer(210367)
    def part_2(self) -> int:
        highest_calories = []
        for i in range(3):
            highest = max(self.calories_per_elves)
            highest_calories.append(highest)
            self.calories_per_elves.remove(highest)
            print(i)

        return sum(highest_calories)

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
