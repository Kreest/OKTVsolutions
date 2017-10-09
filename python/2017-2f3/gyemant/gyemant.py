from functools import lru_cache
n = int(input())

@lru_cache(None) # Just for memoization
def diamond(n):
    if n < 3:
        return 1
    return sum([diamond(i) for i in range(1, n//2+1)]) + (n % 2) # see txt why

print(diamond(n))
