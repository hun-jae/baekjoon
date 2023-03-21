from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

visited = [[False for _ in range(n)] for _ in range(m)]
nearGraph = [[set() for _ in range(n)] for _ in range(m)]
nearList = []
sizeDict = {}
wall = [1, 2, 4, 8]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
cnt = 0
max_ = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            que = deque([])
            cnt += 1
            size = 1
            que.append([i, j])
            while que:
                x, y = que.popleft()
                for nearRoomNum in nearGraph[x][y]:
                    if nearRoomNum == cnt: continue  # 옆에 있는 방의 번호가 자신의 방의 번호면 넘어감
                    nearList.append([nearRoomNum, cnt])
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        if (graph[x][y] // wall[d]) % 2 == 0: #짝수일때 즉 벽이 없을 때
                            visited[nx][ny] = True
                            que.append([nx, ny])
                            size += 1
                        else: #벽이 있을 때
                            nearGraph[nx][ny].add(cnt)
            sizeDict[cnt] = size
            max_ = max(max_ ,size)

#print(sizeDict)
nearSet = set(list(map(tuple,nearList)))
#print(nearSet)
maxSumSize = 0
for i, j in nearSet:
    maxSumSize = max(maxSumSize, sizeDict[i] + sizeDict[j])
print(cnt)
print(max_)
print(maxSumSize)
