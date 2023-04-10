from heapq import heappush as pu, heappop as po
import sys
input = sys.stdin.readline
small = []
big = []
n = int(input())
mid = int(input())
print(mid)
for i in range(1, n):
    cur = int(input())
    if cur > mid: #들어온값이 큼
        pu(big, cur)
    else:
        pu(small, -cur)

    if len(small) - len(big) == 1:
        pu(big, mid)
        mid = -po(small)
    elif len(big) - len(small) == 2:
        pu(small, -mid)
        mid = po(big)
    print(mid)