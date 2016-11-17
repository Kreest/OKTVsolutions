import sys
sys.setrecursionlimit(50000)
memo = {}

def a(n):
    if n < 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n * a(n - 1) + (n - 1) * a(n - 2)
    return memo[n]

def aiter(n):
    an1 = 1
    an2 = 1
    y = 0
    for x in range(2,n + 1):
        y = x * an2 + (x - 1) * an1
        an1 = an2
        an2 = y
        yield y

print(*aiter(50))
