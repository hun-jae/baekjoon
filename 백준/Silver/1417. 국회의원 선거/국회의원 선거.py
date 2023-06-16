n = int(input())
votes = [int(input()) for _ in range(n)]
cnt = 0
while True:
    max_ = 0
    idx = 0
    for i in range(1, n):
        if votes[i] > max_:
            max_ = votes[i]
            idx = i
    if max_ >= votes[0]:
        votes[0] += 1
        votes[idx] -= 1
        cnt += 1
    else:
        break
print(cnt)