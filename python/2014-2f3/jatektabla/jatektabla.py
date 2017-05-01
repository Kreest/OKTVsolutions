#!/usr/bin/env python3
def back(a):
	return a[:-1]

def left(a):
	i = 1
	while a[-i] == 0:
		a[-i] = 2
		i += 1
	if a[-i] == 1:
		a[-i] = 0
	else:
		a[-i] = 1
	return a

def right(a):
	i = 1
	while a[-i] == 2:
		a[-i] = 0
		i += 1
	if a[-i] == 0:
		a[-i] = 1
	else:
		a[-i] = 2
	return a

input()
steps = list(map(int, input().split()))

result = []
for step in steps:
	if step in {0, 1, 2}:
		result.append(step)
	elif step == 3:
		result = back(result)
	elif step == 4:
		result = left(result)
	elif step == 5:
		result = right(result)
print(*result)
