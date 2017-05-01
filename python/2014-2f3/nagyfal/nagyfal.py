#!/usr/bin/env python3
import sys
from itertools import groupby
N, M = map(int, input().split())
guards = [int(x) for x in sys.stdin.readlines()]

posts = [False] * N
for i in set(guards):
	posts[i-1] = True

u = set()
extras = len([x for x in guards if all([x in u, not u.add(x)])]) #Can't use `and` because of short-circuit breakdown

defended = [a and b for a, b in zip(posts[1:], posts[:-1])]
dset = [1 for k, v in groupby(defended) if k]
print(len(dset))

guarded = [a or b for a, b in zip(posts[1:], posts[:-1])]
gset = [1 for k, v in groupby(guarded) if k]
print(len(gset))


gnotd = [g and not d for g, d in zip(guarded, defended)]
free = [not g for g in guarded]




doublespots = [a and b for a, b in zip(free[:-1], free[1:])]
doublespots.append(free[-1])
doublespots = [a, b, c in zip(free[:-1], free[])]
print(doublespots)