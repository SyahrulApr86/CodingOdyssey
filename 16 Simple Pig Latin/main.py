# https://www.codewars.com/kata/520b9d2ad5c005041100000f/
import string

def pig_it(text):
    if not text: return ""
    text_list = text.split()
    res = []

    for word in text_list:
        if word in string.punctuation:
            res.append((word))
            continue

        res.append(word[1:] + word [0] + 'ay')

    return " ".join(res)

# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])

# import string
#
# def pig_it(text):
#     if not text: return ""
#     return " ".join([word[1:] + word[0] + 'ay' if word not in string.punctuation else word for word in text.split()])

# def pig_it(text):
#     return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())