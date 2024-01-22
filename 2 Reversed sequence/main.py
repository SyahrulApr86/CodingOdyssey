# https://www.codewars.com/kata/5a00e05cc374cb34d100000d/solutions/python

def reverse_seq(n):
    lst = []

    while n > 0:
        lst.append(n)
        n -= 1

    return lst


# def reverse_seq(n):
#     return [x for x in range(n, 0, -1)] # --> range will return list in python 2.x

