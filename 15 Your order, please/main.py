# https://www.codewars.com/kata/55c45be3b2079eccff00010f/

def order(sentence):
    if not sentence: return ""

    words = sentence.split(' ')
    res = []

    for i in range(1, 10):
        for word in words:
            if str(i) in word:
                res.append(word)

    return " ".join(res)
