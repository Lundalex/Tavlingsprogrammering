# LÖST

import math

N, M = map(int, input().split())

sol = [1] * N

numSpikes = math.floor(N/M)

if numSpikes * M == N:
    print("NO")
    exit()

print("YES")
for i in range(math.floor(N/M)):
    sol[(i+1)*M-1] = int(1e6)

for val in sol:
    print(str(val) + " ")