def part1(data):
    manifold = data.copy()
    count = 0

    for i in range(len(manifold) - 1):
        for j in range(len(manifold[i])):
            beam_entry = manifold[i][j] == "S"
            beam_unblocked = manifold[i][j] == "|" and manifold[i + 1][j] == "."
            beam_split = manifold[i][j] == "|" and manifold[i + 1][j] == "^"

            if beam_entry or beam_unblocked:
                manifold[i + 1] = manifold[i + 1][:j] + "|" + manifold[i + 1][j + 1 :]

            if beam_split:
                manifold[i + 1] = (
                    manifold[i + 1][: j - 1]
                    + "|"
                    + manifold[i + 1][j]
                    + "|"
                    + manifold[i + 1][j + 2 :]
                )

                count += 1

    return count


def part2(data):
    manifold = []

    for string in data:
        row = []

        for char in string:
            row.append(char)

        manifold.append(row)

    for i in range(len(manifold) - 1):
        for j in range(len(manifold[i])):
            beam_entry = manifold[i][j] == "S"
            beam_unblocked = type(manifold[i][j]) == int and manifold[i + 1][j] == "."
            beam_combined = (
                type(manifold[i][j]) == int and type(manifold[i + 1][j]) == int
            )
            beam_split = type(manifold[i][j]) == int and manifold[i + 1][j] == "^"

            if beam_entry:
                manifold[i + 1][j] = 1

            elif beam_unblocked:
                manifold[i + 1][j] = manifold[i][j]

            elif beam_combined:
                manifold[i + 1][j] += manifold[i][j]

            elif beam_split:
                left = manifold[i + 1][j - 1]
                right = manifold[i + 1][j + 1]

                if type(left) != int:
                    manifold[i + 1][j - 1] = manifold[i][j]

                else:
                    manifold[i + 1][j - 1] += manifold[i][j]

                if type(right) != int:
                    manifold[i + 1][j + 1] = manifold[i][j]

                else:
                    manifold[i + 1][j + 1] += manifold[i][j]

    count = 0

    for value in manifold[-1]:
        if type(value) == int:
            count += value

    return count
