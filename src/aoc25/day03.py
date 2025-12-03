def part1(data):
    total = 0

    for bank in data:
        max_digit_one = 0
        max_digit_two = 0

        for i in range(len(bank) - 1):
            battery_one = int(bank[i])

            if battery_one > max_digit_one:
                max_digit_one = battery_one
                start = i + 1

        for i in range(start, len(bank)):
            battery_two = int(bank[i])

            if battery_two > max_digit_two:
                max_digit_two = battery_two

        joltage = int(str(max_digit_one) + str(max_digit_two))
        total += joltage

    return total


def find_max_digit(bank, start, digits_remaining, joltage):
    search_area = bank[start : len(bank) - digits_remaining]
    max_digit = 0

    for i in range(len(search_area)):
        battery = int(search_area[i])

        if battery > max_digit:
            max_digit = battery
            search_index = i + 1

    start += search_index
    joltage += str(max_digit)

    return joltage, start


def part2(data):
    total = 0

    for bank in data:
        joltage = ""
        start = 0

        for i in range(12):
            digits_remaining = 12 - i - 1
            joltage, start = find_max_digit(bank, start, digits_remaining, joltage)

        total += int(joltage)

    return total
