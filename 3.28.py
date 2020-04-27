import sys
import os
from os import path



print([i for i in range(8, -9, -2)])


def factors(n):
    k = 1
    while k*k < n:
        if n % k == 0:
            yield k
            yield n//k
        k += 1
    if k * k == n:
        yield k

stack = list[input()]
for i in range(len(stack)):
    print(stack.pop())

if __name__ == '__main__':
    print(factors(20))
