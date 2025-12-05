def count_rolls(i, j, data):
    top = i == 0
    bottom = i == len(data) - 1
    left = j == 0
    right = j == len(data[i]) - 1

    corner = any(
        (
            top and left,
            top and right,
            bottom and left,
            bottom and right,
        )
    )

    if corner:
        return 0

    rolls = 0

    if top:
        if data[i][j - 1] == "@":
            rolls += 1

        if data[i][j + 1] == "@":
            rolls += 1

        for char in data[i + 1][j - 1 : j + 2]:
            if char == "@":
                rolls += 1

    elif bottom:
        if data[i][j - 1] == "@":
            rolls += 1

        if data[i][j + 1] == "@":
            rolls += 1

        for string in data[i - 1][j - 1 : j + 2]:
            if string == "@":
                rolls += 1

    elif left:
        if data[i - 1][j] == "@":
            rolls += 1

        if data[i + 1][j] == "@":
            rolls += 1

        for string in data[i - 1 : i + 2]:
            if string[j + 1] == "@":
                rolls += 1

    elif right:
        if data[i - 1][j] == "@":
            rolls += 1

        if data[i + 1][j] == "@":
            rolls += 1

        for string in data[i - 1 : i + 2]:
            if string[j - 1] == "@":
                rolls += 1

    else:
        for string in data[i - 1 : i + 2]:
            for char in string[j - 1 : j + 2]:
                if char == "@":
                    rolls += 1

        rolls -= 1

    return rolls


def part1(data):
    total = 0

    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "@" and count_rolls(i, j, data) < 4:
                total += 1

    return total


def collect_rolls(data):
    total = 0
    new_data = []

    for i in range(len(data)):
        string = ""

        for j in range(len(data[i])):
            if data[i][j] == "@":
                if count_rolls(i, j, data) < 4:
                    total += 1
                    string += "x"

                else:
                    string += "@"

            else:
                string += data[i][j]

        new_data.append(string)

    return total, new_data


def part2(data):
    total = 0
    rolls = 1

    while rolls > 0:
        rolls, data = collect_rolls(data)
        total += rolls

    return total
