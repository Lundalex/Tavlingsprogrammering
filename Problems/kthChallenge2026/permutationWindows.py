# EJ LÖST (men typ?)

N = int(input())
A = [int(a) for a in input().split()]

T = [n for n in range(1, N+1)] # [1 ... N]
f = [0] * N

for k in range(1, N+1): #  [1 ... N]
    
    # find candidates
    candIdxs = []
    for i, a in enumerate(A):
        if k == a:
            candIdxs.append(i)
    
    # test candidates
    for candIdx in candIdxs:
        targets = T[:(k-1)] # 1 <= n <= k-1
        
        # search to the right
        pointer = candIdx + 1
        while pointer < N and A[pointer] in targets:
            targets.remove(A[pointer])
            pointer += 1
        
        # search to the left
        pointer = candIdx - 1
        while pointer >= 0 and A[pointer] in targets:
            targets.remove(A[pointer])
            pointer -= 1
        
        # store the result
        if len(targets) == 0:
            f[k-1] = 1
            break

m = sum(f)
print(m)

s = ""
for i, fk in enumerate(f):
    if fk == 1:
        s += str(i+1) + " " # k = i+1
if s != "":
    print(s)