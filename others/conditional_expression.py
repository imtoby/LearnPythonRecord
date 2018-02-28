# -*- coding: utf-8 -*-
# Created by: ZhaoDongshuang
# Created on: 18-2-12
import math


def test_source_01(x):
    if x > 0:
        y = math.log(x)
    else:
        y = float('nan')


def test_source_01_conditional(x):
    y = math.log(x) if x > 0 else float('nan')


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_conditional(n):
    return 1 if n == 0 else n * factorial(n - 1)


def capitalize_all(t):
    # res = []
    # for s in t:
    #     res.append(s.capitalize())
    # return res
    return [s.capitalize() for s in t]


def only_upper(t):
    # res = []
    # for s in t:
    #     if s.isupper():
    #         res.append(s)
    # return res
    return [s for s in t if s.isupper()]


def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)


def substract(d1, d2):
    # res = dict()
    # for key in d1:
    #     if key not in d2:
    #         res[key] = None
    # return res
    return set(d1) - set(d2)


def has_duplicates(t):
    # d = {}
    # for x in t:
    #     if x in d:
    #         return True
    #     d[x] = True
    # return False
    return len(set(t)) < len(t)


def uses_only(word, available):
    # for letter in word:
    #     if letter not in available:
    #         return False
    # return True
    return set(word) <= set(available)


# def all_anagrams(filename):
#     # d = {}
#     # for line in open(filename):
#     #     word = line.strip().lower()
#     #     t = signature(word)
#     #     # if t not in d:
#     #     #     d[t] = [word]
#     #     # else:
#     #     #     d[t].append(word)
#     #     d.setdefault(t, []).append(word)
#     # return d
#     d = defaultdict(list)
#     for line in open(filename):
#         word = line.strip().lower()
#         t = signature(word)
#         d[t].append(word)
#     return d


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self,):
        return '(%g, %g)' % (self.x, self.y)


# class Pointier(Point):
#     #  在这里添加更多的方法


def print_all(*args, **kwargs):
    print(args, kwargs)


print_all(1, 2.0, '3')
