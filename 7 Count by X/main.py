# https://www.codewars.com/kata/5513795bd3fafb56c200049e

def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [i for i in range(x, x * (n + 1), x)]

