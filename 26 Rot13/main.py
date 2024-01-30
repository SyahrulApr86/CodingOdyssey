# https://www.codewars.com/kata/530e15517bc88ac656000716/train/python

def rot13(message):
    res = ''
    for i in message:
        if 'A' <= i <= 'Z':
            ascii_i = ord(i) + 13
            if ascii_i > ord('Z'):
                ascii_i -= 26
        elif 'a' <= i <= 'z':
            ascii_i = ord(i) + 13
            if ascii_i > ord('z'):
                ascii_i -= 26
        else:
            res += i
            continue
        res += chr(ascii_i)
    return res



# print(rot13('aA bB zZ 1234 *!?%'))


# print(rot13('z'))