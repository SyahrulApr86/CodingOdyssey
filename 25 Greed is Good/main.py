# https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/python

def score(dice):
    count = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
    }

    for point in dice:
        count[str(point)] += 1

    score = (count['1'] // 3 * 1000 + count['2'] // 3 * 200 + count['3'] // 3 * 300 + count['4'] // 3 * 400 +
             count['5'] // 3 * 500 + count['6'] // 3 * 600 + count['1'] % 3 * 100 + count['5'] % 3 * 50)

    return score


print(score([3, 3, 3, 3, 3]))
