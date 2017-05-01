#!/usr/bin/env python3
import sys
from collections import defaultdict
N, R = map(int, input().split())
Income = tuple(map(int, input().split()))
Connections = [tuple(map(int, x.split())) for x in sys.stdin.readlines()]
adj_list = defaultdict(lambda: defaultdict(lambda: 0))
for a, b, cost in Connections:
	adj_list[b][a] = cost
	adj_list[a][b] = cost
S = R
values = list(Income)
stack = []
parentmap = {}
pathmap = {x: [x] for x in range(1, N+1)}

def DFS(v):
	labels = set()
	S = []
	S.append(v)
	while S:
		v = S.pop()
		if v not in labels:
			labels.add(v)
			for child, cost in adj_list[v].items():
				if child not in labels:
					S.append(child)
					parentmap[child] = (v, cost)
		stack.append(v)
DFS(R)

while stack:
	child = stack.pop()
	if child != R:
		parent, cost = parentmap[child]
		if values[child-1] >= cost:
			values[parent-1] += values[child-1] - cost
			pathmap[parent].extend(pathmap[child])
print(values[R-1])
print(len(pathmap[R]))
print(*pathmap[R])