from aoc25 import core, day03

data = core.load_file("./test_data/03.txt")


def test_part1():
    assert day03.part1(data) == 357


def test_part2():
    assert day03.part2(data) == 3121910778619
