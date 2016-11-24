#!/usr/bin/env python3
M, d = map(int, input().split())
entries = [int(x) for x in input().split()]
magicnumber = sum(entries) // d
rem = sum(entries) % d
if d == 1:
	print(*[item for sublist in [[x+1] * y for x, y in enumerate(entries)] for item in sublist])
elif d == 2:
	pass
elif d == 3:
	pass