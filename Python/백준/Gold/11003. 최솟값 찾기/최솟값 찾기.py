import sys
from collections import deque

input = sys.stdin.readline

dq = deque()
res = []

N, L = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    if dq and dq[0] <= i - L:
        dq.popleft()

    while dq and A[dq[-1]] >= A[i]:
        dq.pop()

    dq.append(i)
    res.append(str(A[dq[0]]))

print(" ".join(res))
