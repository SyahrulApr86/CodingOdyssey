# https://www.codewars.com/kata/51e056fe544cf36c410000fb
from string import punctuation
def top_3_words(text):
    punctuation_list = list(punctuation.replace("'", ""))
    dct_words = dict()
    word = ""
    for char in text:
        if char not in ("\n", " ") and char not in punctuation_list:
            word += char
        else:
            if word != "":
                if word not in dct_words:
                    dct_words[word] = 1
                else:
                    dct_words[word] += 1
                word = ""

    return dct_words

print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""))
