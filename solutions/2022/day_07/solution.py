# prompt: https://adventofcode.com/2022/day/7

# from typing import Tuple
from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple
from ...base import StrSplitSolution, answer


def list_files_until_next_command(console: List[str], current_idx: int) -> List[str]:
    lines = []
    for line in console[current_idx + 1 :]:
        if line.split(" ")[0] == "$":
            return lines
        lines.append(line)
    return lines


@dataclass
class Directory:
    depth: list
    total: int


class Solution(StrSplitSolution):
    _year = 2022
    _day = 7

    # @answer(1234)
    def part_1(self) -> int:
        pass

    # @answer(1234)
    def part_2(self) -> int:
        pass

    @answer((1582412, 3696336))
    def solve(self) -> Tuple[int, int]:
        console = self.input
        depths = []
        directories: List[Directory] = []
        current_size = 0
        for idx, line in enumerate(console):
            pre, *post = line.split(" ")
            if pre == "$":
                if post[0] == "cd":
                    # Go up or down one directory
                    if post[-1] == "..":
                        depths.pop(-1)
                    else:
                        depths.append(post[-1])
                elif post[0] == "ls":
                    current_size = 0
                    files = list_files_until_next_command(console, idx)
                    for file in files:
                        label, filename = file.split(" ")
                        if label != "dir":
                            current_size += int(label)
                    # Save current directory's size
                    directories.append(
                        Directory(depth=deepcopy(depths), total=current_size)
                    )
        # Add child dir's size into parent
        items = sorted(directories, key=lambda x: len(x.depth), reverse=True)
        for child in items:
            parent_dir = child.depth[:-1]
            for parent in items:
                if parent.depth == parent_dir and parent is not child:
                    parent.total += child.total
        total = 0
        for item in items:
            if item.total <= 100_000:
                total += item.total

        # PART 2
        total_space = 70_000_000
        required_space = 30_000_000
        disk_space = max([d.total for d in directories])

        to_delete = abs(total_space - required_space - disk_space)

        bigger_than_to_delete = sorted(
            [*filter(lambda x: x.total >= to_delete, directories)],
            key=lambda x: x.total,
            reverse=True,
        )
        return total, bigger_than_to_delete[-1].total
