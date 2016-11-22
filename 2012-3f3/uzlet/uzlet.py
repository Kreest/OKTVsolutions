#!/usr/bin/env python3
import sys
N, R = map(int, input().split())
Income = tuple(map(int, input().split()))
Connections = [tuple(map(int, x.split())) for x in sys.stdin.readlines()]
Q = set(Connections)
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
			for x in [x for x in filter(lambda x: x[0] == v or x[1] == v, Connections)]:
				a, b, cost = x
				source = a if b != v else b
				child = a if b == v else b
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