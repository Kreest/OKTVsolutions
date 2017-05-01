#!/usr/bin/env python3
def rectangles(N, M):
	for j in range(N):
		for i in range(M):
			for y in range(j, N):
				for x in range(i, M):
					yield (i, j, x, y)

import sys
N, M, K = map(int, input().split(" "))

grid = [list(map(int, line.split())) for line in sys.stdin]
presum = [[sum(line[:i+1])for i in range(M)] for line in grid]

tdpresum = []
for line in range(N):
	temp = []
	for x in range(M):
		if line == 0:
			temp.append(presum[line][x])
		else:
			temp.append(presum[line][x] + tdpresum[line-1][x])
	tdpresum.append(temp)

def trees(rec):
	i, j, x, y = rec
	trees = tdpresum[y][x]
	if i > 0:
		trees -= tdpresum[y][i-1]
	if j > 0:
		trees -= tdpresum[j-1][x]
	if i > 0 and j > 0:
		trees += tdpresum[j-1][i-1]
	return trees
def area(rec):
	i, j, x, y = rec
	return (x-i+1)*(y-j+1)
print("t")
carea = 100000
minr = (-1, -1, -1, -1)
for r in rectangles(N, M):
	if trees(r) == K:
		a = area(r)
		if a < carea:
			carea = a
			minr = map(lambda x: x+1, r)

i, j, x, y = minr
print(j, i, y, x)