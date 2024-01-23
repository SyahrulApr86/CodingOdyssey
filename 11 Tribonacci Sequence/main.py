# https://www.codewars.com/kata/556deca17c58da83c00002db

def tribonacci(signature, n):
    if n == 0:
        return []
    if n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    elif n == 3:
        return [signature[0], signature[1], signature[2]]

    res = signature
    for _ in range(4, n+1):
        res.append(res[-1] + res[-2] + res[-3])

    return res



