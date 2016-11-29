#!/usr/bin/env python3
import sys
from collections import defaultdict
N, M, A, E = map(int, input().split())
start = A
goal = E
wtf = sys.stdin.readlines()
dangerous = set(map(int, wtf[-1].split()))
connections = defaultdict(lambda: set())
for x in wtf[:-1]:
	a, b = map(int, x.split())
	connections[a].add(b)
	connections[b].add(a)

stack = [A]
Q = set(range(1, N+1))
steps = {x: 100000 for x in Q}
prev = {}
steps[start] = 0
while Q:
	u = min(steps.keys() & Q, key = steps.get)
	Q.remove(u)
	for v in connections[u] & Q:
		alt = steps[u] + int(v in dangerous)
		if alt < steps[v]:
			steps[v] = alt
			prev[v] = u

path = []
u = goal
while u in prev:
	path.append(u)
	u = prev[u]
path.append(start)

print(steps[goal])
print(len(path) - 2) 
print(*reversed(path))