#!/usr/bin/env python3
M, d = map(int, input().split())
entries = [int(x) for x in input().split()]
magic = sum(entries) // d
print(magic)
rem = sum(entries) % d
if d == 1:
	print(*[item for sublist in [[x+1] * y for x, y in enumerate(entries)] for item in sublist])
elif d == 2:
	m = [[0 for _ in range(0, magic)] for _ in range(0, M)]

	for i in range(1, M):
		for j in range(0, magic):
			if entries[i] > j:
				m[i][j] = m[i-1][j]
			else:
				m[i][j] = max(m[i-1][j], m[i-1][j-entries[i]]+i)
	print(m)
elif d == 3:
	pass