def part1(data):
    id_ranges_str = [string.split("-") for string in data[0].split(",")]
    id_ranges_int = [(int(first), int(last)) for first, last in id_ranges_str]

    count = 0

    for id_range_int in id_ranges_int:
        for id_int in range(id_range_int[0], id_range_int[1] + 1):
            id_str = str(id_int)

            if id_str.startswith("0"):
                continue

            if len(id_str) % 2 != 0:
                continue

            midpoint = len(id_str) // 2

            if id_str[:midpoint] == id_str[midpoint:]:
                count += id_int

    return count


def get_prime_factorisation(n):
    i = 2
    prime_factorisation = []

    while i**2 <= n:
        if n % i == 0:
            prime_factorisation.append(i)
            n //= i

        else:
            i += 1

    prime_factorisation.append(n)

    return prime_factorisation


def get_prime_products(n):
    # TODO: simplify
    # Convert prime factorisation into (prime, exponent) pairs
    primes = []
    factors = get_prime_factorisation(n)

    for prime in factors:
        if not primes or primes[-1][0] != prime:
            primes.append([prime, 1])

        else:
            primes[-1][1] += 1

    # Enumerate all divisors by choosing exponents for each prime
    products = set([1])

    for prime, exponent in primes:
        new = set()

        for base in products:
            product = 1

            for _ in range(exponent + 1):
                new.add(base * product)
                product *= prime

        products = new

    products = {d for d in products if d > 1}

    return products


def part2(data):
    id_ranges_str = [string.split("-") for string in data[0].split(",")]
    id_ranges_int = [(int(first), int(last)) for first, last in id_ranges_str]

    count = 0

    for id_range_int in id_ranges_int:
        for id_int in range(id_range_int[0], id_range_int[1] + 1):
            id_str = str(id_int)

            if len(id_str) < 2:
                continue
            products = get_prime_products(len(id_str))

            if len(products) < 2:
                match = True

                for i in range(len(id_str) - 1):
                    if id_str[i] != id_str[i + 1]:
                        match = False
                        break

                if match:
                    count += id_int

            else:

                for product in products:
                    match = True
                    sequence_length = len(id_str) // product

                    for i in range(len(id_str) - sequence_length):
                        if id_str[i] != id_str[i + sequence_length]:
                            match = False
                            break

                    if match:
                        count += id_int
                        break

    return count
