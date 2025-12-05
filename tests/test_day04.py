from aoc25 import core, day04

data = core.load_file("./test_data/04.txt")


def test_part1():
    assert day04.part1(data) == 13


def test_part2():
    assert day04.part2(data) == 43
