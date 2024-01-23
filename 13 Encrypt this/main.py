# https://www.codewars.com/kata/5848565e273af816fb000449/train/python

def encrypt_this(text):
    if not text:
        return ""

    cip = ""
    words = text.split()
    for i in range(len(words[:-1])):
        if len(words[i]) == 0:
            cip += " "
        elif len(words[i]) == 1:
            cip += str(ord(words[i][0])) + ' '
        elif len(words[i]) == 2:
            cip += str(ord(words[i][0])) + words[i][-1] + ' '
        else:
            cip += str(ord(words[i][0])) + words[i][-1] + words[i][2:-1] + words[i][1] + ' '

    if len(words[-1]) == 0:
        cip += ""
    elif len(words[-1]) == 1:
        cip += str(ord(words[-1][0]))
    elif len(words[-1]) == 2:
        cip += str(ord(words[-1][0])) + words[-1][-1]
    else:
        cip += str(ord(words[-1][0])) + words[-1][-1] + words[-1][2:-1] + words[-1][1]

    return cip

