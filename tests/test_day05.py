from aoc25 import core, day05

data = core.load_file("./test_data/05.txt")


def test_part1():
    assert day05.part1(data) == 4


def test_part2():
    assert day05.part2(data) == 19
