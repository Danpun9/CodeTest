import sys
from sys import stdout

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = []
res_sum = sys.maxsize

for l in range(n - 2):
    r = n - 1
    mid = l + 1

    while mid < r:
        sum = arr[l] + arr[mid] + arr[r]

        if abs(sum) < abs(res_sum):
            res = [arr[l], arr[mid], arr[r]]
            res_sum = sum

        if sum == 0:
            sys.stdout.write(f"{res[0]} {res[1]} {res[2]}\n")
            exit(0)
        elif sum < 0:
            mid += 1
        else:
            r -= 1

sys.stdout.write(f"{res[0]} {res[1]} {res[2]}\n")