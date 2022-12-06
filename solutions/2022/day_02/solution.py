# prompt: https://adventofcode.com/2022/day/2

# from typing import Tuple
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 2

    @answer(13675)
    def part_1(self) -> int:
        strategies = self.input

        score_table = {
            "choice": {"X": 1, "Y": 2, "Z": 3},
            "outcome": {"lose": 0, "draw": 3, "win": 6},
        }

        # fmt: off
        outcome_table = {
            'A X': 'draw', 'A Y': 'win', 'A Z': 'lose',
            'B X': 'lose', 'B Y': 'draw', 'B Z': 'win',
            'C X': 'win', 'C Y': 'lose', 'C Z': 'draw'
        }

        def calculate_score(input: str) -> int:
            choice_score = score_table['choice'][input[-1]]
            outcome_score = score_table['outcome'][outcome_table[input]]
            return choice_score + outcome_score

        score = 0
        for strategy in strategies:
            score += calculate_score(strategy)
        return score

    @answer(14184)
    def part_2(self) -> int:
        strategies = self.input
        # fmt: off
        intended_outcome = {
            'A': 1, 'B': 2, 'C': 3,
            'X': 0, 'Y': 3, 'Z': 6,
        }

        # fmt: off
        intended_choice = {
            'A X': 'C', 'A Y': 'A', 'A Z': 'B',
            'B X': 'A', 'B Y': 'B', 'B Z': 'C',
            'C X': 'B', 'C Y': 'C', 'C Z': 'A'
        }

        def calculate_intended_score(input: str) -> int:
            choice_score = intended_outcome[intended_choice[input]]
            outcome_score = intended_outcome[input[-1]]
            return choice_score + outcome_score

        score = 0
        for strategy in strategies:
            score += calculate_intended_score(strategy)

        return score

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
