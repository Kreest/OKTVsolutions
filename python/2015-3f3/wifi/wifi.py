#!/usr/bin/env python3

N, H = map(int, input().split())
R = tuple(map(int, input().split()))

start = R[0]
i = 0
res = []
while i < len(R):
	while i < len(R) and start + H >= R[i]:
		i += 1
	else:
		res.append(i)
		midpoint = R[i-1]
		while i < len(R) and midpoint + H >= R[i]:
			i += 1
		else:
			if i < len(R):
				start = R[i]
print(len(res))
print(*res)