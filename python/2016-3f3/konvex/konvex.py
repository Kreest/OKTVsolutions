#!/usr/bin/env python3
from random import sample, choice
from itertools import groupby
def sign(x):
	return (x>0) - (x<0)

def cross(a, line):
	x, y = a
	a, b = line
	x0, y0 = a
	x1, y1 = b
	return ((x-x0)*(y1-y0)) - ((y-y0) * (x1-x0)) 

def between(a, line):
	p, q = line
	x1, y1 = p
	x2, y2 = q
	p1 = [(x1, y1), (x1+(y2-y1),y1-(x2-x1))]
	p2 = [(x2-(y1-y2),y2+(x1-x2)), (x2, y2)]
	return cross(a, p1) * cross(a, p2) > 0



N = int(input())
order = {}
for i in range(0, N):
	t = tuple(map(int, input().split()))
	a, b = t
	order[t] = i+1
points = list(order)
line = sample(points, 2)
print(line)
s = sorted(points, key = lambda x: cross(x, line))
spl = {k: tuple(v) for k, v in groupby(s, lambda x: sign(cross(x, line)))}
print(spl, len(spl))