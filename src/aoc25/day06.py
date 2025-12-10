def part1(data):
    rows = [string.split(" ") for string in data]
    columns = {}

    for i in range(len(rows)):
        count = 0

        for string in rows[i]:
            if len(string) > 0:
                if count not in columns:
                    columns[count] = [string]

                else:
                    columns[count] += [string]

                count += 1

        count = 0

    for column in columns.values():
        operator = column[-1]

        if operator == "+":
            add = 0

            for string in column[:-1]:
                add += int(string)

            count += add

        elif operator == "*":
            mul = 1

            for string in column[:-1]:
                mul *= int(string)

            count += mul

    return count


def part2(data):
    worksheet = [row[::-1] for row in data]
    operators = [character for character in worksheet[-1] if character != " "]
    operator_ranges = [(None, -1)]

    for i in range(len(worksheet[-1])):
        if worksheet[-1][i] != " ":
            end = i + 1
            start = operator_ranges[-1][1] + 1

            operator_ranges.append((start, end))

    operator_ranges.pop(0)

    groups = []

    for i in range(len(operator_ranges)):
        start = operator_ranges[i][0]
        end = operator_ranges[i][1]

        group = []

        for j in range(start, end):
            string = ""

            for row in worksheet[:-1]:
                string += row[j]

            if len(string.strip()) > 0:
                group.append(int(string.strip()))

        groups.append(group)

    total = 0

    for i in range(len(operators)):
        operator = operators[i]
        group = groups[i]

        if operator == "+":
            add = 0

            for number in group:
                add += number

            total += add

        elif operator == "*":
            mul = 1

            for number in group:
                mul *= number

            total += mul

    return total
