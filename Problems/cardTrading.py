# LÖST

def intput():
    return map(int, input().split())

# take inputs
N, D = intput()
names = []
cardSets = []
for i in range(N):
    name, _ = input().split() # _ = number of cards
    cardSet = input().split()
    
    names.append(name)
    cardSets.append(cardSet)

# handle trades
for i in range(D):
    nameA, cardA, nameB, cardB = input().split()
    indexA, indexB = names.index(nameA), names.index(nameB)
    
    cardSets[indexA].remove(cardA)
    cardSets[indexA].append(cardB)
    
    cardSets[indexB].remove(cardB)
    cardSets[indexB].append(cardA)

# output results
for cardSet in cardSets:
    cardSet.sort()
    
    s = ""
    for card in cardSet:
        s += card
        s += " "
    print(s)