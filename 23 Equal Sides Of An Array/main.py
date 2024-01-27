# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

def find_even_index(arr):
    for sep in range(len(arr)):
        sum_left = 0
        sum_right = 0
        for num in range(sep):
            sum_left += arr[num]

        for num in range(len(arr) - 1, sep, -1):
            sum_right += arr[num]

        if sum_left == sum_right:
            return sep

    return -1


def find_even_index_2(arr):
    sum_left = 0
    sum_right = sum(arr)

    for i, num in enumerate(arr):
        sum_right -= num
        if sum_left == sum_right:
            return i
        sum_left += num

    return -1


import random
import timeit

# Generate a random array of length 1000
random_array = [random.randint(-100, 100) for _ in range(1000)]

# Test the speed of both functions
time_original = timeit.timeit(lambda: find_even_index(random_array), number=100)
time_optimized = timeit.timeit(lambda: find_even_index_2(random_array), number=100)

print(time_original, time_optimized)