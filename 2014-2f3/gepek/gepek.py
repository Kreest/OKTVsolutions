#!/usr/bin/env python3
from math import ceil
from itertools import groupby
N, M = map(int, input().split())
orders = list(map(int, input().split()))
t = sorted(enumerate(orders), key = lambda x: x[1])
g = [list(v) for k, v in groupby(t, key = lambda x: x[1])]

gepek = 1
munkak = 0
for day in g:
	munkak += len(day)
	gepek = max(gepek, ceil(munkak / day[0][1]))
print(gepek)

toprint = {}
cday = 1
cgep = 1
for day in g:
	for order in day:
		toprint[order[0]] = (cday, cgep)
		cgep += 1
		if cgep == 13:
			cgep = 1
			cday += 1
for y in toprint:
	print(*toprint[y])
