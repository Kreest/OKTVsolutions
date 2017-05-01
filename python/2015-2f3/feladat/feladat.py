#!/usr/bin/env python3
from itertools import permutations
from math import factorial
N, M = map(int, input().split())
goal = tuple(map(int, input().split()))
order = list(range(1, N+1))
i = 1
k = factorial(N) // factorial(N-M)
print(k, k)
n = N
for x in goal: 
    k //= n
    n -= 1
    j = order.index(x)
    i += j * k
    del order[j]

order = list(range(1, N+1))
k = factorial(N) // factorial(N-M)
z = k
n = N - 1
res = []
for x in range(M):
    print(i)
    z = z // n
    print(z)
    n -= 1
    v = i // z
    print(v)
    res.append(order[v])
    del order[v]
    i = i % z
print(res)