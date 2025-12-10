import os

import aoc25
from aoc25 import *


# FIXME: Do not strip lines when reading files as some puzzles rely on whitespace
def load_file(path):
    with open(path) as file:
        data = [line.strip() for line in file.readlines()]

    return data


class Solver:
    def __init__(self):
        self.data = {}
        self.solutions = {}

    def load_data(self, path):
        files = os.listdir(path)

        for file in files:
            key = file.split(".")[0]
            value = load_file(os.path.join(path, file))

            self.data[key] = value

    def run(self):
        for n in self.data.keys():
            module = getattr(aoc25, f"day{n}")

            solution_part1 = module.part1(self.data[n])
            solution_part2 = module.part2(self.data[n])

            self.solutions[f"Day {n}"] = (solution_part1, solution_part2)
            self.solutions[f"Day {n}"] = (solution_part1, solution_part2)
