N = int(input())
build_time = [-1] * N
build_order = [[-1] * N for _ in range(N)]
real_time = [-1] * N

q = []

for i in range(N):
    arr = list(map(int, input().split()))
    t = arr[0]
    build_time[i] = t
    if arr[1] < 0:
        real_time[i] = build_time[i]
        continue

    for j in range(1, len(arr) - 1):
        build_order[i][j-1] = arr[j] - 1
    q.append(i)

while q:
    cur = q.pop(0)
    flag = True

    for build in build_order[cur]:
        if build == -1:
            break
        if real_time[build] == -1:
            q.append(cur)
            flag = False
            break

    if not flag:
        continue

    for build in build_order[cur]:
        if build == -1:
            break
        real_time[cur] = max(real_time[cur], build_time[cur] + real_time[build])

for i in range(N):
    print(real_time[i])
