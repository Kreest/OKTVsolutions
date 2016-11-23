#!/usr/bin/env python3
import sys
from collections import defaultdict
import bisect
pairs = defaultdict(lambda: [])
N, M = map(int, input().split())
for line in sys.stdin.readlines():
	a, b = map(int, line.split())
	bisect.insort(pairs[a], b)
