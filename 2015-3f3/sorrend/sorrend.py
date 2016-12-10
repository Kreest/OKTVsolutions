#!/usr/bin/env python3
memo = {} #Memoization is storing the functions calculated output for a certain input, then on next call just returning it from memory. Vastly improves recursion speed. More fun that rewriting iteratively

def perm(n):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = (n-1) * perm(n-1) + (n-2) * perm(n-2) #The complicated part is deriving this formula, explained in formula.txt
    return memo[n]

print(perm(50))
