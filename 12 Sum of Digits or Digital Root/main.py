# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    while n // 10 > 0: n = sum(list(map(int, list(str(n)))))
    return n

# def digital_root(n):
# 	return n%9 or n and 9