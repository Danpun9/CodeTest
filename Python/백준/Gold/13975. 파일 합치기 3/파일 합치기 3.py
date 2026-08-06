import sys
import heapq

input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    heapq.heapify(arr)

    total_cost = 0

    while len(arr)>1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)

        total_cost += first + second

        heapq.heappush(arr, first + second)

    print(total_cost)