#!/usr/bin/env python3
import sys

inp = sys.stdin.read().split() #read everything from the standard input, split it into lines
lt = list(map(int, inp[1:])) #read each line except the first into a list, mapping the elements to integers
ln = len(lt)

maxx = 0
maxsum = 0
for x in range(1,ln+1):
	csum = 0
	for y in range(0,ln//2): #ln is guaranteed to be even. // is integer division
		csum += (y+1)*(lt[(x+y) % ln]) #go through the list forwards, reset to zero if over ln
		csum += (y+1)*(lt[x-1-y]) #go backwards, yay for python indexing magic
	
	if csum > maxsum:
		maxsum = csum
		maxx = x
print(maxx)