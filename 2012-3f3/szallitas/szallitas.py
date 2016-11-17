#!/usr/bin/env python3
#Parsing
import sys

N, M, source, goal = map(int, input().split())
paths = [list(map(int, x.split())) for x in sys.stdin.read().split("\n")]
source -= 1
goal -= 1

#Make a matrix
matrix = [[0 for x in range(N)] for y in range(N)]
for x in paths:
	matrix[x[0]-1][x[1]-1] = x[2]
	matrix[x[1]-1][x[0]-1] = x[2]

#Wonderful Dijkstra
Q = set(range(0, N))
width = [0] * N
prev = [-1] * N

width[source] = 1001
while Q:
	u = max(Q, key = lambda x: width[x])
	Q.discard(u)

	for v in [near for near in range(0, N) if matrix[u][near] > 0 and near in Q]:
		alt = min(width[u], matrix[u][v])
		if alt > width[v]:
			width[v] = alt
			prev[v] = u


t = goal
S = []
while prev[t] >= 0:
	S = [t] + S
	t = prev[t]
S = [source] + S
S = [x+1 for x in S]


print(width[goal])
print(*S)