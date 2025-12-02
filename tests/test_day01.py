from aoc25 import core, day01

data = core.load_file("./downloads/tests/01.txt")


def test_part1():
    assert day01.part1(data) == 3


def test_part2():
    assert day01.part2(data) == 6
