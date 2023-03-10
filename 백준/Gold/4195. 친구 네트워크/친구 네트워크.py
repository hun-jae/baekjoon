import sys
input = sys.stdin.readline
T = int(input())
#answer = []
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
            hash1[a] = cnt1
            hash1[b] = cnt1
            list1[cnt1] = cnt2
            list2[cnt2] += 2
            cnt1 += 1
            cnt2 += 1
            #print(2)
            ans.append(2)
        elif a not in hash1:
            tmpb = -1
            curIdx = hash1[b]
            cur = list1[hash1[b]]  # 현재 그룹 번호
            while True:
                if curIdx == cur:
                    tmpb = cur
                    break
                curIdx = cur
                cur = list1[curIdx]
            hash1[a] = tmpb
            list2[list1[tmpb]] += 1
            #print(list2[list1[hash1[a]]])
            ans.append(list2[list1[hash1[a]]])
        elif b not in hash1:
            tmpa = -1
            curIdx = hash1[a]
            cur = list1[hash1[a]]  # 현재 그룹 번호
            while True:
                if curIdx == cur:
                    tmpa = cur
                    break
                curIdx = cur
                cur = list1[curIdx]
            tmpb = -1
            hash1[b] = tmpa
            list2[list1[tmpa]] += 1
            #print(list2[list1[hash1[a]]])
            ans.append(list2[list1[tmpa]])
        elif a in hash1 and b in hash1:
            tmpa = -1
            curIdx = hash1[a]
            cur = list1[hash1[a]] #현재 그룹 번호
            while True:
                if curIdx == cur:
                    tmpa = cur
                    break
                curIdx = cur
                cur = list1[curIdx]
            tmpb = -1
            curIdx = hash1[b]
            cur = list1[hash1[b]]  # 현재 그룹 번호
            while True:
                if curIdx == cur:
                    tmpb = cur
                    break
                curIdx = cur
                cur = list1[curIdx]
            if tmpa == tmpb: #유니온파인드를 통해 그룹이 같다면 그냥 답이라고 체크해줌
                #print(list2[list1[hash1[a]]])
                ans.append(list2[list1[tmpa]])
                continue
            # b가 들어있는 그룹(list1)의 명수 포인터(list2에 대한)를 a가 들어있는 그룹의 포인터와 같게 해줌
            list2[list1[tmpa]] += list2[list1[tmpb]]
            list2[list1[tmpb]] = list2[list1[tmpa]]
            list1[tmpb] = list1[tmpa]
            #print(list2[list1[hash1[a]]])
            ans.append(list2[list1[tmpa]])
    print(*ans,sep="\n")

