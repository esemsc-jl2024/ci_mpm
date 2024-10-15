from functools import cache
__all__ = ['my_sum','factorial','my_sin']

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1

def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot

def my_sin(x, terms=10):
    sine = 0
    for i in range(terms):
        sign = (-1) ** i
        sine += sign * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    
    return sine
