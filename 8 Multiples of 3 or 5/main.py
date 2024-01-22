# # https://www.codewars.com/kata/514b92a657cdc65150000006/python

import timeit

def solution(number):
    if number < 0:
        return 0

    _sum = 0
    i = 3
    while i < number:
        _sum += i
        i += 3

    i = 5
    while i < number:
        if i % 3 == 0:
            i += 5
            continue
        _sum += i
        i += 5
    return _sum

def solution2(number): # --> this is very clever way
    a3 = (number-1)/3
    a5 = (number-1)/5
    a15 = (number-1)/15
    result = (a3*(a3+1)/2)*3 + (a5*(a5+1)/2)*5 - (a15*(a15+1)/2)*15
    return result

# # Setting up the testing environment
# setup_code = "from __main__ import solution, solution2"
#
# # Testing the first function
# time_solution = timeit.timeit("solution(10000)", setup=setup_code, number=10000)
#
# # Testing the second function
# time_solution2 = timeit.timeit("solution2(10000)", setup=setup_code, number=10000)
# print(time_solution, time_solution2)
#
