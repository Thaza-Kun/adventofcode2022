# prompt: https://adventofcode.com/2022/day/5

# from typing import Tuple
from collections import defaultdict
from copy import deepcopy
from dataclasses import dataclass
from typing import List, Tuple
from ...base import TextSolution, answer


@dataclass
class Instruction:
    moves: int
    before: int
    after: int


class Solution(TextSolution):
    _year = 2022
    _day = 5

    # @answer("CNSZFDVLJ")
    # def part_1(self) -> int:
    #     pass

    # @answer(1234)
    # def part_2(self) -> int:
    #     pass

    # @answer((1234, 4567))
    def solve(self) -> Tuple[int, int]:
        crates, instructions = self.input.split("\n\n")
        instructions = instructions.split("\n")
        stacks: dict = defaultdict(list)
        stack_ids, *layers = crates.splitlines()[::-1]
        stack_ids = [x.strip() for x in stack_ids.split("  ")]

        for layer in layers:
            for stack, top_crate in zip(range(len(stack_ids)), layer.split(" ")):
                # !! Added empty crates `[_]` to the input
                if top_crate != "[_]":
                    stacks[stack + 1].append(top_crate[1])
        steps: List[Instruction] = list()
        for instruction in instructions:
            tokens = instruction.split(" ")
            steps.append(
                Instruction(
                    moves=int(tokens[1]), before=int(tokens[3]), after=int(tokens[5])
                )
            )
        stack2 = deepcopy(stacks)
        for step in steps:
            to_move = []
            for move in range(step.moves):
                top_crate = stacks[step.before].pop(-1)
                to_move.append(top_crate)
            stacks[step.after].extend(to_move)

        for step in steps:
            to_move = stack2[step.before][-step.moves :]
            stack2[step.before] = stack2[step.before][: -step.moves]
            stack2[step.after].extend(to_move)
        top_crates = []
        top_crates2 = []
        for crate, crate2 in zip(stacks.values(), stack2.values()):
            top_crates.append(crate[-1])
            top_crates2.append(crate2[-1])
        return ("".join(top_crates), "".join(top_crates2))
