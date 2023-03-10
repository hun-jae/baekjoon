import sys
input = sys.stdin.readline
T = int(input())

def find(a):
    curIdx = hash1[a]
    cur = list1[hash1[a]]  # 현재 그룹 번호
    while True:
        if curIdx == cur:
            tmpa = cur
            break
        curIdx = cur
        cur = list1[curIdx]
    return cur

for tc in range(1, T+1):

    F = int(input())
    hash1 = {}

    list1 = [-1] * F
    list2 = [0] * F
    cnt1 = 0  # hash 그룹 카운트
    cnt2 = 0
    ans = []

    for _ in range(F):
        a, b = input().split()
        if a not in hash1 and b not in hash1:
            tmpa = hash1[a] = cnt1
            hash1[b] = cnt1
            list1[cnt1] = cnt2
            list2[cnt2] += 2
            cnt1 += 1
            cnt2 += 1

        elif a not in hash1:
            tmpa = tmpb = find(b)
            hash1[a] = tmpb
            list2[list1[tmpb]] += 1

        elif b not in hash1:
            tmpa = find(a)
            hash1[b] = tmpa
            list2[list1[tmpa]] += 1

        elif a in hash1 and b in hash1:
            tmpa, tmpb = find(a), find(b)
            if tmpa == tmpb:
                ans.append(list2[list1[tmpa]])
                continue
            list2[list1[tmpa]] += list2[list1[tmpb]]
            list2[list1[tmpb]] = list2[list1[tmpa]]
            list1[tmpb] = list1[tmpa]

        ans.append(list2[list1[tmpa]])
    print(*ans,sep="\n")
