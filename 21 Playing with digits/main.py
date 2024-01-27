# https://www.codewars.com/kata/5552101f47fc5178b1000050

def dig_pow(n, p):
    # n_k = sum([num**(p+idx) for idx, num in enumerate(list(map(int, n)))])
    n_k = 0
    for idx, num in enumerate(list(map(int, n))): # we not using sum to reduce complexity
        n_k += num**(p+idx)

    if n_k % n == 0:
        return n_k // n
    else:
        return -1

# def dig_pow(n, p):
#   s = 0
#   for i,c in enumerate(str(n)):
#      s += pow(int(c),p+i)
#   return s/n if s%n==0 else -1


