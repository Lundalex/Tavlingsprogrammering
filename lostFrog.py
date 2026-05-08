# LÖST

import math

class UnionFind:
    def __init__(self, n):
        self.parents = [n for n in range(n)]
        self.ranks = [0] * n
        self.members = [[n] for n in range(n)]

    def find(self, a):
        if self.parents[a] != a: # climb up the tree until node 'a' has itself as its parent.
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a] # union representative
    
    def getMembers(self, a):
        return self.members[self.find(a)]
    
    def getRoots(self):
        roots = []
        for parent, i in enumerate(self.parents):
            if parent == i:
                roots.append(i)
        return roots
    
    def union(self, a, b): 
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a == root_b:
            return
        
        rank_a = self.ranks[root_a]
        rank_b = self.ranks[root_b]
        
        if rank_a < rank_b: # add a -> b
            self.parents[root_a] = root_b
            self.members[root_b] += self.members[root_a]
            self.members[root_a] = []
        elif rank_b < rank_a: # add b -> a
            self.parents[root_b] = root_a
            self.members[root_a] += self.members[root_b]
            self.members[root_b] = []
        else: # choose to add b -> a. Also increase the rank by 1
            self.parents[root_b] = root_a
            self.members[root_a] += self.members[root_b]
            self.members[root_b] = []
            self.ranks[root_a] += 1

# UnionFind-test:

# def intput(txt):
#     return int(input(txt))

# numElements = intput("Number of elements: ")
# unionFind = UnionFind(numElements)
# while (cmd := input("Input cmd (f, u, q): ")) != 'q':
#     if cmd == 'f':
#         print("parent:", unionFind.find(intput("a: ")))
#     elif cmd == 'u':
#         unionFind.union(intput("a: "), intput("b: "))
#     else:
#         pass

# LostFrog solution:

def distance(a, b):
    diff = [a[0]-b[0], a[1]-b[1]]
    return math.sqrt(diff[0]**2 + diff[1]**2)

def superCrappyHasPossiblePath(d, L, humans):
    unionFind = UnionFind(len(humans))
    
    # form groups of close humans
    # katastrofal komplexitet
    for i, human in enumerate(humans):
        for root in unionFind.getRoots():
            members = unionFind.getMembers(root)
            for member in members:
                if distance(human, humans[member]) < 2*d:
                    unionFind.union(root, i)
    
    # check for possible blockages
    for root in unionFind.getRoots():
        edges = {'L': False, 'B': False, 'R': False, 'T': False}
        
        for member in unionFind.getMembers(root):
            human = humans[member]
        
            if human[0] < d: # Left
                edges['L'] = True
            if human[1] < d: # Bottom
                edges['B'] = True
            if human[0] > L - d: # Right
                edges['R'] = True
            if human[1] > L - d: # Top
                edges['T'] = True
        
        # blocked = (L + B) || (B + T) || (T + R) || (L + R)
        if (edges['L'] and edges['B']) or (edges['B'] and edges['T']) or (edges['T'] and edges['R']) or (edges['L'] and edges['R']):
            return False # This group blocks all paths from (0, 0) to (L, L)
    return True

def hasPossiblePath(d, L, humans):
    humanUnions = UnionFind(len(humans))
    groupEdges = {} # {root: {'L': False, 'B': False, 'R': False, 'T': False}}
    
    # Contruct groups of neaby humans
    for i, human in enumerate(humans):
        for j, otherHuman in enumerate(humans[0:i]):
            if distance(human, otherHuman) < 2*d:
                humanUnions.union(i, j)
    
    # Check edges
    for i, human in enumerate(humans):
        root = humanUnions.find(i)
        if root not in groupEdges:
            groupEdges[root] = {'L': False, 'B': False, 'R': False, 'T': False}
        edges = groupEdges[root]
        if human[0] < d: # Left
            edges['L'] = True
        if human[1] < d: # Bottom
            edges['B'] = True
        if human[0] > L - d: # Right
            edges['R'] = True
        if human[1] > L - d: # Top
            edges['T'] = True
    
    for edges in groupEdges.values():
        # blocked = (L + B) || (B + T) || (T + R) || (L + R)
        if (edges['L'] and edges['B']) or (edges['B'] and edges['T']) or (edges['T'] and edges['R']) or (edges['L'] and edges['R']):
            return False # This group blocks all paths from (0, 0) to (L, L)
    
    return True



L, N = map(int, input("").split())
humans = [tuple(map(int, input("").split())) for _ in range(N)]
d = 0.1
delta = L/2

l, r = 0, L
tol = 1e-7
while (r-l) >= tol:
    m = (l + r) / 2
    
    if hasPossiblePath(m, L, humans):
        l = m
    else:
        r = m
d = (l + r) / 2
print(d)
