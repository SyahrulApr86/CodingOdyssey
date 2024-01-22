# https://www.codewars.com/kata/57f780909f7e8e3183000078/python

def grow(arr):
    result = 1
    for i in arr:
        result *= i
    return result
#
# import math
# def grow(arr):
#     return math.prod(arr)

# from functools import reduce
#
# def grow(arr):
#     return reduce(lambda x, y: x * y, arr)
#
# from functools import reduce
# from operator import mul
#
# def grow(arr):
#     return reduce(mul, arr, 1)
#
# from math import prod as grow
#
# from operator import mul
#
# def grow(arr):
#     return reduce(mul, arr)

