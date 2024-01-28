# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):
    zero_count = 0
    res = []

    for i in lst:
        if i != 0:
            res.append(i)
            continue
        zero_count += 1

    res.extend([0]*zero_count)
    return res

