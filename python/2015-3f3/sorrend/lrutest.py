#!/usr/bin/env python3
from functools import lru_cache #Fancy tool for memoization

@lru_cache()
def perm(n):
    if n <= 2:
        return 1
    return (n-1) * perm(n-1) + (n-2) * perm(n-2)

print(perm(int(input()))%1000000000)