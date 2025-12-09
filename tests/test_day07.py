from aoc25 import core, day07

data = core.load_file("./test_data/07.txt")


def test_part1():
    assert day07.part1(data) == 21


def test_part2():
    assert day07.part2(data) == 40
