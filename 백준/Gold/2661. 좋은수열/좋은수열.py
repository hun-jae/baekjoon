n = int(input())
ans = []
def bt(depth):
    if depth==n:
        print(*ans,sep="")
        exit(0)
    for i in range(1,4):
        ans.append(i)
        la = len(ans)
        for i in range(1, la//2 + 1):
            if ans[la-i:] == ans[la-(2*i):la-i]:
                break
        else:
            bt(depth+1)
        ans.pop()
bt(0)
