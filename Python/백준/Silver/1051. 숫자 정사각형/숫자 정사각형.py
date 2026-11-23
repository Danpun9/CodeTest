import sys

input = sys.stdin.readline

n,m = map(int, input().split())

arr = [list(map(int, list(input().strip()))) for _ in range(n)]

res = 1

for dxy in range(1, min(n,m)):
    for i in range(n):
        if i + dxy >= n:
            break

        for j in range(m):
            if j + dxy >= m:
                break

            if arr[i][j] == arr[i+dxy][j] and arr[i][j+dxy] == arr[i+dxy][j+dxy] and arr[i][j] == arr[i+dxy][j+dxy]:
                res = (dxy+1)**2


print(f"{res}")