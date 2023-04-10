from heapq import heappush as pu, heappop as po
n, m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    adj_list[a].append([c, b])
    adj_list[b].append([c, a])

q = []
visited[1] = True
for c, b in adj_list[1]:
    pu(q, [c, b])
ans = 0
for _ in range(n-1):
    while q:
        c, cur = po(q)
        if visited[cur]:
            continue
        ans += c
        visited[cur] = True
        for cost, next in adj_list[cur]:
            if not visited[next]:
                pu(q, [cost, next])
        break
print(ans)