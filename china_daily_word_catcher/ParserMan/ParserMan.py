__author__ = 'jqly'

import re
import os

import feedparser
import requests


# I can return word and corresponding frequency
def get_word_dict(url):
    d = feedparser.parse(url)

    word_dict = dict()

    for entry in d.entries:
        summary = entry.summary

        word_list = get_word_list(entry.title + ' ' + summary)
        for word in word_list:
            word_dict.setdefault(word, 0)
            word_dict[word] += 1
    return word_dict


# I belong to the function above
def get_word_list(html):
    text = re.compile(r'<*?>').sub(' ', html)
    word_list = re.findall(r'\b[a-z]+\b', text)

    return [w.lower() for w in word_list]


# I crawl china daily for others are kind of blocked
def spider_man():
    target_url = 'http://www.chinadaily.com.cn/rss/'
    r = requests.get(target_url)
    page = r.text
    pattern = re.compile(r'<h6><a href=".*?xml">(.*?)</a></h6>', re.S | re.M)
    items = re.findall(pattern, page)
    return items


url_list = spider_man()
print('Total number of urls: %d' % len(url_list))
d = dict()
counter = 1
for url in url_list:
    dd = get_word_dict(url)
    for item in dd:
        d.setdefault(item, 0)
        d[item] += dd[item]
    print('\nFinish url-%d: %s' % (counter, url))
    counter += 1

print('\nGenerating word list...')
word_list = sorted(d.items(), key=lambda x: x[1])

# Create a word list file
if os.path.isfile('words_you_should_learn.txt'):
    os.remove('words_you_should_learn.txt')
word_list_file = open('words_you_should_learn.txt', 'a')

# This file is a set of words you have learned, empty for illiterate
# Make this file in words_you_know directory
# The output file is DIY word list
word_learned_set = set()
if os.path.isfile('.\words_you_know\words_you_know.txt'):
    words_learned_file = open('.\words_you_know\words_you_know.txt', 'r')
    for word in words_learned_file.readlines():
        word_learned_set.add(word.strip('\n'))

for word in word_list:
    if word[0] not in word_learned_set:
        print('%-20s%d' % (word[0], word[1]), file=word_list_file)
