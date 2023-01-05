# prompt: https://adventofcode.com/2022/day/8

# from typing import Tuple
from collections import defaultdict
from typing import List
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2022
    _day = 8

    @answer(1700)
    def part_1(self) -> int:
        grid: List[str] = self.input
        grid_T: List[str] = list(zip(*grid))  # Transpose grid
        visible_trees: int = 0
        for idx_row, row in enumerate(grid):
            # Count edges (top & bottom)
            if idx_row == 0 or idx_row == len(grid_T) - 1:
                visible_trees += len(row)
            else:
                for idx_col, tree in enumerate(row):
                    # Count edges (left & right)
                    if idx_col == 0 or idx_col == len(row) - 1:
                        visible_trees += 1
                    else:
                        left = [int(x) for x in row[:idx_col]]
                        right = [int(x) for x in row[idx_col + 1 :]]
                        top = [int(x) for x in grid_T[idx_col][:idx_row]]
                        bottom = [int(x) for x in grid_T[idx_col][idx_row + 1 :]]
                        if (
                            max(left) < int(tree)
                            or max(right) < int(tree)
                            or max(top) < int(tree)
                            or max(bottom) < int(tree)
                        ):
                            visible_trees += 1
        return visible_trees

    @answer(470596)
    def part_2(self) -> int:
        grid: List[str] = self.input
        grid_T: List[str] = list(zip(*grid))  # Transpose grid
        score: List[int] = []

        def viewing_distance(this_tree: int, line_of_sight: List[int]) -> int:
            for idx, that_tree in enumerate(line_of_sight, start=1):
                # Return the index of the first tree to be equal
                #       or higher than candidate tree house tree
                if that_tree >= this_tree:
                    return idx
            # Else return the length of the whole line of sight
            return len(line_of_sight)

        for idx_row, row in enumerate(grid):
            # Count edges (top & bottom)
            if idx_row != 0 or idx_row != len(grid_T) - 1:
                for idx_col, tree in enumerate(row):
                    scenic_score: int = 1
                    # Count edges (left & right)
                    if idx_col != 0 or idx_col != len(row) - 1:
                        # normalized to move left to right / top to bottom
                        left = [int(x) for x in row[:idx_col]][::-1]
                        right = [int(x) for x in row[idx_col + 1 :]]
                        top = [int(x) for x in grid_T[idx_col][:idx_row]][::-1]
                        bottom = [int(x) for x in grid_T[idx_col][idx_row + 1 :]]
                        for direction in [left, right, top, bottom]:
                            if len(direction) != 0:
                                scenic_score *= viewing_distance(
                                    this_tree=int(tree), line_of_sight=direction
                                )
                        score.append(scenic_score)
        return max(score)

    # @answer((1234, 4567))
    # def solve(self) -> Tuple[int, int]:
    #     pass
