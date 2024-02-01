# https://www.codewars.com/kata/51e056fe544cf36c410000fb
from string import punctuation


def top_3_words(text):
    punctuation_list = list(punctuation.replace("'", ""))
    dct_words = dict()
    word = ""
    for char in text + ' ':
        if char not in ("\n", " ") and char not in punctuation_list:
            word += char
        else:
            if word != "" and not all(char == "'" for char in word):
                if word.lower() not in dct_words:
                    dct_words[word.lower()] = 1
                else:
                    dct_words[word.lower()] += 1
                word = ""

    return sorted(dct_words, key=dct_words.get, reverse=True)[:3]


import re
from collections import Counter


def top_3_words2(text):
    # Menggunakan regular expression untuk menemukan semua kata yang valid
    # Kata yang valid berarti terdiri dari huruf a-z (case-insensitive) dan mungkin mengandung apostrof
    words = re.findall(r"[a-zA-Z']+(?:'[a-zA-Z]+)*", text.lower())

    # Menghitung frekuensi setiap kata yang valid dengan menggunakan Counter
    word_counts = Counter(words)

    # Mengabaikan kata-kata yang hanya terdiri dari apostrof
    filtered_counts = Counter(
        {word: count for word, count in word_counts.items() if not all(char == "'" for char in word)})

    # Mengambil 3 kata dengan frekuensi tertinggi
    top_three = [word for word, count in filtered_counts.most_common(3)]

    return top_three


from collections import defaultdict
import operator


class Parser(object):
    # Add a trailing whitespace to string for parser generator (see note at end of class)
    def __init__(self, textToParse: str) -> None:
        self.body = textToParse + " "

    # Blackspace: A character to keep; any letter [a-zA-Z] or apostrophy
    def _isBlackspace(self, char: str) -> bool:
        return (char.isalpha() or char == "'")

    # Whitespace: A character to toss out; anything that is not blackspace
    def _isWhitespace(self, char: str) -> bool:
        return (not self._isBlackspace(char))

    # Generator that produces tokens of blackspace that are not all apostrophes
    def tokenizer(self) -> str:
        token, consumingToken = [], False
        for char in self.body:
            if self._isBlackspace(char):
                token.append(char)
                consumingToken = True
            if self._isWhitespace(char) and consumingToken:
                # To be a valid token, the token must contain atleast one letter [a-zA-Z]
                if any(c.isalpha() for c in token):
                    yield ''.join(token)
                token = []
                consumingToken = False
    # end function

    # Note on the parser's addition of the trailing whitespace (in constructor): Manages an
    # edge case when the last character in the body of text to parse is a token.
    #      e.g: 'a b c c c' here 'c' is a valid token, and is the last character in the file
    # Since the trailing whitespace character is concatenated to the body of the text,
    # garantees that 'if self._isWhitespace(char) and consumingToken' is true for this edge
    # case scenario.


# end class


# Given a body of text, get at most the three words with the largest frequency
def top_3_words3(text: str) -> list:
    p = Parser(text)
    counter = defaultdict(int)
    topWords = []

    for token in p.tokenizer():  # get word frequency
        counter[token.lower()] += 1

    for _ in range(3):  # get at most three words with higest freq
        if counter:
            maxKey = max(counter.items(), key=operator.itemgetter(1))[0]
            topWords.append(maxKey)
            counter.pop(maxKey)
        else:
            break

    return topWords


import time
import random
import string
# Generate a long random text
random_text = ' '.join(random.choice(string.ascii_lowercase + "'") for _ in range(1000000))

# Measure and compare execution time
start_time = time.time()
top_3_words(random_text)
time_1 = time.time() - start_time

start_time = time.time()
top_3_words2(random_text)
time_2 = time.time() - start_time

start_time = time.time()
top_3_words3(random_text)
time_3 = time.time() - start_time

print(time_1, time_2, time_3)
