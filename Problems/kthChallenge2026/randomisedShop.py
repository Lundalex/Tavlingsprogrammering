# LÖST 

N, M = map(int, input().split())
C = [int(c) for c in input().split()] # prices
D = [int(d) for d in input().split()] # rewards
G = [D[i]-C[i] for i in range(N)] # gains

I = [[C[i], D[i], G[i]] for i in range(N)] # items

I = list(filter(lambda item: item[2] >= 0, I))

I.sort(key = lambda item: item[0]) # sort by lowest cost

for i in range(len(I)):
    if I[i][0] <= M:
        # buy the item
        M += I[i][2]
    else:
        break

print(M)