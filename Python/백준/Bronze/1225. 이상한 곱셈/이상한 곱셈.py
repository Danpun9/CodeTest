import sys

input = sys.stdin.readline


a, b = input().split()

a = list(map(int, a))
b = list(map(int, b))

res = 0
for i in a:
    for j in b:
        res += i * j

print(res)
