"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

def mul(a, b):
    return a*b

def id(a):
    return a

def add(a, b):
    return a+b

def neg(a):
    return -a

def lt(a, b):
    return a < b

def eq(a, b):
    return a == b

def max(a, b):
    if a < b:
        return b
    return a

def is_close(a, b, eps = 1e-5):
    return abs(a-b) < eps

def sigmoid(a):
    return 1.0/(1.0 + math.exp(-a))

def relu(a):
    return a*lt(0, a)

def log(a):
    return math.log(a)

def exp(a):
    return math.exp(a)

def inv(a):
    return 1 / a

def log_back(x, a):
    return (1 / x) * a

def inv_back(x, a):
    return (-1 / x**2) * a

def relu_back(x, a):
    return (x > 0) * a

def sigmoid_back(x, a):
    return sigmoid(x)*(1 - sigmoid(x)) * a




# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def map(f):
    return lambda a: [f(x) for x in a]

def zipWith(f):
    return lambda a, b: [f(x,y) for (x, y) in zip(a, b)]

def reduce(f, x_0):
    def cycle(a, f, x_0):
        for el in a:
            x_0 = f(x_0, el)
        return x_0

    return lambda a: cycle(a, f, x_0)

def negList(a):
    return map(neg)(a)

def addLists(a, b):
    return zipWith(add)(a, b)

def sum(a):
    return reduce(add, 0)(a)

def prod(a):
    return reduce(mul, 1)(a)


    


# TODO: Implement for Task 0.3.
