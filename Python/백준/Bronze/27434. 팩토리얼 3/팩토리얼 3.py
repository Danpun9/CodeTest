import sys
from sys import stdout

input = sys.stdin.readline
write = sys.stdout.write

n = int(input())

res = 1

for i in range(1, n + 1):
    res *= i

write(str(res))
