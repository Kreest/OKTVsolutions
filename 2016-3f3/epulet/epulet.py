#!/usr/bin/env python3
N, I = map(int, input().split())
size = 3 * 2 ** (N - 1)
res = ""
helper = {(3, 1): ('F', 0), (3, 2): ('P', 0), (3, 3): ('Z', 0), (6, 1): ('FP', 0), (6, 2): ('PF', 0), (6, 3): ('PP', 0), (6, 4): ('PZ', 0), (6, 5): ('ZF', 0), (6, 6): ('ZZ', 0)}
while len(res) < N:
	if (size, I) in helper:
		res += helper[(size, I)][0]
	else:
		if I <= size // 4:
			size //= 4
			res += "FP"
		elif I <= size * 3 / 4:
			I -= size // 4
			size //= 2
			res += "P"
		else:
			I -= size * 3 // 4
			size = size // 4
			res += "Z"
			while len(res) < N and I > size / 2:
				res+="Z"
				I -= size / 2
				size /= 2
			else:
				res+="FP"
				size /= 2
print(res[0:N])