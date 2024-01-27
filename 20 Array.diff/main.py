# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

# def array_diff(a, b):
#     res = []
#     for num in a:
#         if num not in b:
#            res.append(num)
#
#     return res

# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    return [num for num in a if num not in b]
