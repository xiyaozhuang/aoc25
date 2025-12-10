from aoc25 import day06

# FIXME: Replace this with the core file loader once it has been fixed
with open("./test_data/06.txt") as file:
    data = file.read().splitlines()


def test_part1():
    assert day06.part1(data) == 4277556


def test_part2():
    assert day06.part2(data) == 3263827
