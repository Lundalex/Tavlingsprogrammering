# EJ LÖST

N = int(input())
numbers = list(map(int, input().split()))
lenNumbers = len(numbers)

S = 0
A0, A1 = 0, 0
cumsum = 0
k = 0
while k < 5 or (abs(A0 - A1) > 2e-7):
    k += 1
    S += numbers[(k-1) % lenNumbers]
    cumsum += S
    A0, A1 = A1, cumsum / k

print(A1)