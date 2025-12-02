def part1(data):
    count = 0
    position = 50

    for line in data:
        direction = line[0]
        rotation = int(line[1:])

        if direction == "R":
            position += rotation

        elif direction == "L":
            position -= rotation

        position %= 100

        if position == 0:
            count += 1

    return count


def part2(data):
    count = 0
    position = 50

    for line in data:
        direction = line[0]
        rotation = int(line[1:])

        if direction == "R":
            for _ in range(rotation):
                position += 1

                if position % 100 == 0:
                    count += 1

        elif direction == "L":
            for _ in range(rotation):
                position -= 1

                if position % 100 == 0:
                    count += 1

    return count
