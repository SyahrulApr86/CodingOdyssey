# https://www.codewars.com/kata/55aa075506463dac6600010d/train/python

def list_squared(m, n):
    res = []
    for num in range(m, n + 1):
        div = set()
        i = 1
        while i * i <= num:
            if num % i == 0:
                div.add(i ** 2)
                div.add((num // i) ** 2)
            i += 1

        total = sum(div)
        sqr = total ** (1 / 2)

        if sqr % 1 == 0:
            res.append([num, total])

    return res


def list_squared2(m, n):
    res = []
    for num in range(m, n + 1):
        div_squares = set()
        i = 1
        while i * i <= num:
            if num % i == 0:
                div_squares.add(i ** 2)
                if i != num // i:
                    div_squares.add((num // i) ** 2)
            i += 1

        total = sum(div_squares)
        sqr = total ** 0.5

        if int(sqr) == sqr:
            res.append([num, total])

    return res


CACHE = {}


def squared_cache(number):
    if number not in CACHE:
        divisors = [x for x in range(1, number + 1) if number % x == 0]
        CACHE[number] = sum([x * x for x in divisors])
        return CACHE[number]

    return CACHE[number]


def list_squared3(m, n):
    ret = []

    for number in range(m, n + 1):
        divisors_sum = squared_cache(number)
        if (divisors_sum ** 0.5).is_integer():
            ret.append([number, divisors_sum])

    return ret


def list_squared4(m, n):
    out = []
    for i in range(m, n + 1):
        # Finding all divisors below the square root of i
        possibles = set([x for x in range(1, int(i ** 0.5) + 1) if i % x == 0])
        # And adding their counterpart
        possibles.update([i / x for x in possibles])
        # Doubles in the possibles are solved due to the set
        val = sum(x ** 2 for x in possibles)
        # Checking for exact square
        if (int(val ** 0.5)) ** 2 == val: out.append([i, val])
    return out


import timeit

# Comparison setup
m, n = 1, 100000  # lowering the value if you want faster testing
number_of_runs = 100

# Timing each function
times = {
    "list_squared": timeit.timeit(lambda: list_squared(m, n), number=number_of_runs),
    "list_squared2": timeit.timeit(lambda: list_squared2(m, n), number=number_of_runs),
    "list_squared3": timeit.timeit(lambda: list_squared3(m, n), number=number_of_runs),
    "list_squared4": timeit.timeit(lambda: list_squared4(m, n), number=number_of_runs)
}

print(times)
