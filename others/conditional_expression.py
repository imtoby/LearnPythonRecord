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


