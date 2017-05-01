#!/usr/bin/env python3
from collections import defaultdict
from itertools import groupby
N, S, M, F = map(int, input().split())
authors = list(map(int, input().split()))

dependency = defaultdict(lambda: set())
check = defaultdict(lambda: set())
for _ in range(0,N):
	I, J = map(int, input().split())
	dependency[I].add(J)
	check[J].add(I)

#A DFS
dep = []
stack = [M]
discovered = set()
while stack:
	for v in dependency[stack.pop()]:
		if v not in discovered:
			discovered.add(v)
			stack.append(v)
			dep.append(v)
print(len(dep), *dep)

#B DFS
notify = set()
stack = [M]
discovered = set()
while stack:
	for v in check[stack.pop()]:
		if v not in discovered:
			discovered.add(v)
			stack.append(v)
			notify.add(authors[v-1])
ntf = notify-set([authors[M-1]])
print(len(ntf), *ntf)

#C
independent = set(range(1, N+1)) - set(x for x in dependency)
hasindie = [key for key, value in groupby(sorted(independent, key = lambda x: authors[x-1]),  key = lambda x: authors[x-1])]
indies = []
for dev in hasindie:
	modules = [module+1 for module, auth in enumerate(authors) if auth == dev]
	isindie = True
	for mod in modules:
		if dependency[mod]:
			for m in dependency[mod]:
				if m not in modules:
					isindie = False
	if isindie:
		indies.append(dev)
if indies:
	print(indies[0])
else:
	print(-1)