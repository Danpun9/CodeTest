import sys

input = sys.stdin.readline

n = (int(input()) // 100) * 100
f = int(input())

for i in range(100):
    if (n + i) % f == 0:
        print(f"{i:02d}")
        break