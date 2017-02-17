#!/usr/bin/env python3
import sys

dist = int(input().split()[1])
points = sorted([tuple(map(int, x.split())) for x in sys.stdin.readlines()])
print(points)