#!/usr/bin/env python3
from collections import defaultdict
N, M = map(int, input().split())
buildblocks = list(map(int, input().split()))
targets = set(map(int, input().split()))
mem = defaultdict(lambda: False)
limit = max(targets)
for x in buildblocks:
	multiple = x
	while multiple <= limit:
		mem[multiple] = True
		multiple += x

for x in (x for x in range(1, limit+1) if x not in mem):
	if any([mem[x-i % 30000] for i in buildblocks]):
		mem[x] = True
print(targets & set(x for x in mem))