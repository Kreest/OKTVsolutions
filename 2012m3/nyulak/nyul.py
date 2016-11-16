#!/usr/bin/env python3
import sys

inp = sys.stdin.read().split("\n")
yrs, maxage, _ = map(int, inp[0].split())

table = {i+1: 0 if len(x) == 1 else x[1] for i, x in [[i, list(map(int, x.split()))] for i, x in enumerate(inp[1:])]}
nyulak = [int(x.split()[0]) for x in inp[1:]]
for x in range(0,yrs):
	newnyulak = sum([nyulak[x-1] * table[x] for x in range(1, maxage+1)])
	nyulak = [newnyulak] + nyulak
	nyulak.pop()
print(sum(nyulak) % 1000000)