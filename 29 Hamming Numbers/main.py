# https://www.codewars.com/kata/526d84b98f428f14a60008da/train/python

def is_hamming_number(n):
    if n == 1:
        return True
    if n <= 0:
        return False
    for prime in [2, 3, 5]:
        while n % prime == 0:
            n /= prime
    return n == 1


def hamming_naive(N):  # --> not optimal and will cause time limit exceeded
    count, number = 0, 1
    while True:
        if is_hamming_number(number):
            count += 1
            if count == N:
                return number
        number += 1


import heapq


def hamming_deque(N):
    heap = [1]
    seen = {1}
    val = None

    for _ in range(N):
        val = heapq.heappop(heap)
        for factor in [2, 3, 5]:
            next_val = val * factor
            if next_val not in seen:
                heapq.heappush(heap, next_val)
                seen.add(next_val)

    return val


import heapq


def hamming_heap(N):
    heap = [1]
    seen = {1}
    val = None

    for _ in range(N):
        val = heapq.heappop(heap)
        for factor in [2, 3, 5]:
            next_val = val * factor
            if next_val not in seen:
                heapq.heappush(heap, next_val)
                seen.add(next_val)

    return val
