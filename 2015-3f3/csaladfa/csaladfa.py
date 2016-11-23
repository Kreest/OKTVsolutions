#!/usr/bin/env python3
import sys
from functools import reduce

N, M = map(int, input().split())
parents = {a: (b, c) for a, b, c in (map(int, item.split()) for item in sys.stdin.readlines())}


childless = set(range(1, N+1)) - {x[0] for x in parents.values()} - {x[1] for x in parents.values()} #Childless islanders are those who are in the base set, but are nowhere in the parents dict values
ancestries = [] #Ancestors of each childless islander
for node in childless:
	ancestors = set()
	stack = [node]

	while stack:
		v = stack.pop()
		if v in parents:
			for x in parents[v]:
				stack.append(x)
				ancestors.add(x)
	ancestries.append(ancestors)


t = reduce(lambda x, y: x & y, ancestries, set(range(1, N+1))) #Get the intersection of all ancestors with the base set

if t:
	print(len(t))
	print(*sorted(t))
else:
	print(0)