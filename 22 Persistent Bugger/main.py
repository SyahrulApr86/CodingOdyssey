# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

def persistence(n):
    op = 0

    while n // 10 > 0:
        temp = 1
        for num in list(map(int, str(n))):
            temp *= num

        n = temp
        op += 1

    return op


# def persistence(n):
#     if n < 10: return 0
#     mult = 1
#     while (n > 0):
#         mult = n % 10 * mult
#         n = n // 10
#     return persistence(mult) + 1
