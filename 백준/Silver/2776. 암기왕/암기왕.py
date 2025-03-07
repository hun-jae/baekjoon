import sys

T = int(input())

for _ in range(T):
    N = int(input())
    note = sorted(list(map(int, sys.stdin.readline().split())))
    M = int(input())
    note2 = list(map(int, sys.stdin.readline().split()))
    result = [-1 for _ in range(M)]
    for j in range(M):
        l, r = 0, N - 1
        while l <= r:
            mid = (l + r) // 2
            if note2[j] == note[mid]:
                result[j] = 1
                break
            if note2[j] < note[mid]:
                r = mid - 1
            elif note2[j] > note[mid]:
                l = mid + 1

        if result[j] == -1:
            result[j] = 0
   
    for e in result:
        print(e)

