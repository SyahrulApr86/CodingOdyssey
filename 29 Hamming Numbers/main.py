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



from collections import deque

def hamming_queue(N):
    hamming_numbers = [1] * N
    q2, q3, q5 = deque([2]), deque([3]), deque([5])
    i2 = i3 = i5 = 0

    for i in range(1, N):
        next_hamming = min(q2[0], q3[0], q5[0])
        hamming_numbers[i] = next_hamming
        if next_hamming == q2[0]:
            i2 += 1
            q2.popleft()
            q2.append(hamming_numbers[i2] * 2)
        if next_hamming == q3[0]:
            i3 += 1
            q3.popleft()
            q3.append(hamming_numbers[i3] * 3)
        if next_hamming == q5[0]:
            i5 += 1
            q5.popleft()
            q5.append(hamming_numbers[i5] * 5)

    return hamming_numbers[-1]


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


def hamming_number_DP(N):
    hamming_numbers = [1] * N  # Inisialisasi array untuk menyimpan N Hamming numbers
    i2 = i3 = i5 = 0  # Indeks untuk kelipatan 2, 3, dan 5

    # Nilai awal untuk kelipatan 2, 3, dan 5
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5

    for i in range(1, N):
        # Hamming number berikutnya adalah minimum dari ketiga kelipatan
        next_hamming_number = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        hamming_numbers[i] = next_hamming_number

        # Update nilai kelipatan jika mereka telah digunakan
        if next_hamming_number == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = hamming_numbers[i2] * 2
        if next_hamming_number == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = hamming_numbers[i3] * 3
        if next_hamming_number == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = hamming_numbers[i5] * 5

    return hamming_numbers[-1]  # Mengembalikan Hamming number ke-N


