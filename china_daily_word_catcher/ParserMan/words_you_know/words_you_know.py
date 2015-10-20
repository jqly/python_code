__author__ = 'jqly'

import re
import os


# words.txt is a classic word list file you must familiar with
# I sieve for english words
with open('words.txt', 'r', encoding='utf8') as f:
    raw_word_list = f.readlines()
    word_list = set()
    for string in raw_word_list:
        lis = re.findall(r'\b([a-zA-Z]+)\s', string)
        if lis:
            word_list.add(lis[0])

if os.path.isfile('words_you_should_learn.txt'):
    os.remove('words_you_should_learn.txt')

with open('words_you_know.txt', 'a', encoding='utf8') as f:
    for word in word_list:
        print(word.lower(), file=f)
