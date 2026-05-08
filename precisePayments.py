# Catastrophic complexity version (works theoretically though)

import math

def intput():
    return int(input())

def multiples(denom, ceil):
    maxMultiple = math.floor(ceil / denom)
    for i in range(maxMultiple+1):
        yield i*denom

def compareAll(denoms, target, values):
    denom = denoms.pop()
    
    for value in multiples(denom, target):
        newValues = values + [value]
        
        if len(denoms) > 0:
            if compareAll(list(denoms), target, newValues):
                return True
        
        else: # len(denoms) == 0
            if sum(newValues) == target:
                return True
    
    return False

# N = intput()
# denoms = list(map(int, input().split()))

# for target in reversed(range(int(1e6)+1)):
#     solutionFound = compareAll(list(denoms), target, [])
#     if not solutionFound:
#         print(target)
#         exit()

# print("no change necessary")



# Better scan-like algo
N = int(input())
denoms = list(map(int, input().split()))

possibles = [False for _ in range(int(1e6)+1)]
possibles[0] = True

# scan through the 1e6 x N
for denom in denoms:
    for i in range(denom, len(possibles)):
        if possibles[i - denom]:
            possibles[i] = True

# find first False
for i in reversed(range(len(possibles))):
    if not possibles[i]:
        print(i)
        exit()

print("no change necessary")