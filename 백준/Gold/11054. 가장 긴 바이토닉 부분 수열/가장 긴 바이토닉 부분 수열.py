n = int(input())
list_ = list(map(int, input().split()))
upList = [0 for i in range(1001)]
downList = [0 for i in range(1001)]
for i in list_:
    upList[i] = max(upList[:i])+1
    if i < 1000:
        downList[i] = max(upList[i], max(downList[i+1:])+1)
    else:
        downList[i] = max(upList[i], 1)
print(max(downList))