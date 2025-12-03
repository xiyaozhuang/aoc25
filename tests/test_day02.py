from aoc25 import core, day02

data = core.load_file("./test_data/02.txt")


def test_part1():
    assert day02.part1(data) == 1227775554


def test_part2():
    assert day02.part2(data) == 4174379265
