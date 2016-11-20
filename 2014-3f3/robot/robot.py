#!/usr/bin/env python3
import sys
debug = sys.argv[1] == "debug"

dist = int(input().split()[1])
grid = [[0 for i in range(dist+1)] for j in range(dist+1)]
lines = sys.stdin.readlines()
mem = {}
k = 1
for line in lines:
	a, b = map(int, line.split())
	if (a+b-2) <= dist:
		grid[a-1][b-1] = 1
	mem[(a, b)] = k
	k+=1

for i in range(dist):
	for j in range(dist):
		if (i+j) <= dist:
			grid[i][j] += max(grid[i-1][j], grid[i][j-1])

diag = [grid[dist-i][i] for i in range(dist+1)]
best = max(diag)
bp = diag.index(best)
x, y = (dist - bp, bp)
if debug:
	print(x, y)

coords = []
if (x+1, y+1) in mem:
		coords.append(mem[(x+1, y+1)])
while x > 0 or y > 0:
	if x > 0 and (grid[x][y] == grid[x-1][y]):
		x -= 1
	elif y > 0 and (grid[x][y] == grid[x][y-1]):
		y -= 1
	elif x > 0 and (grid[x][y] - 1 == grid[x-1][y]):
		x -= 1
	elif y > 0 and (grid[x][y] - 1 == grid[x][y-1]):
		y -= 1
	if (x+1, y+1) in mem:
		coords.append(mem[(x+1, y+1)])

print(best)
print(*coords)