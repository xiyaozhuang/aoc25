def part1(data):
    fresh = []
    available = []

    for string in data:
        if len(string) < 1:
            continue

        if "-" in string:
            start, end = string.split("-")
            fresh.append((int(start), int(end)))

        else:
            available.append(int(string))

    fresh_ingredients = 0

    for i in range(len(available)):
        for j in range(len(fresh)):
            if fresh[j][0] <= available[i] <= fresh[j][1]:
                fresh_ingredients += 1

                break

    return fresh_ingredients


def part2(data):
    fresh_ranges = []

    for string in data:
        if "-" in string:
            start, end = string.split("-")
            fresh_ranges.append([int(start), int(end)])

    intersections = 1

    while intersections > 0:
        intersections = 0
        i = 0

        while i < len(fresh_ranges):
            for j in range(i):
                range_after = fresh_ranges[j][0] > fresh_ranges[i][1]
                range_before = fresh_ranges[j][1] < fresh_ranges[i][0]

                if not (range_after or range_before):
                    intersections += 1

                    new_range_start = min(fresh_ranges[i][0], fresh_ranges[j][0])
                    new_range_end = max(fresh_ranges[i][1], fresh_ranges[j][1])

                    fresh_ranges[i] = [new_range_start, new_range_end]

                    fresh_ranges.pop(j)
                    i -= 1

                    break

            i += 1

    fresh_ingredients = 0

    for start, end in fresh_ranges:
        fresh_ingredients += end - start + 1

    return fresh_ingredients
