from collections import deque

K = int(input())
W, H = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(H)]

visited = [[[False for _ in range(K +1)] for _ in range(W)] for _ in range(H)]
# for line in visited:
#     for k in line:
#         print(*k)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
horse_dx = [-2, -2, -1, -1, 1, 1, 2, 2]
horse_dy = [-1, 1, -2, 2, -2, 2, -1, 1]


def bfs():
    que = deque([(0, 0, 0)])
    visited[0][0][0] = True
    cnt = 1
    while que:
        size = len(que)
        for _ in range(size):
            x, y, k = que.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][k] and not graph[nx][ny]:
                    if nx == H - 1 and ny == W - 1:
                        return cnt
                    visited[nx][ny][k] = True
                    que.append([nx, ny, k])
            if k < K:
                for d in range(8):
                    nx = x + horse_dx[d]
                    ny = y + horse_dy[d]
                    if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny][k + 1] and not graph[nx][ny]:
                        if nx == H - 1 and ny == W - 1:
                            return cnt
                        visited[nx][ny][k + 1] = True
                        que.append([nx, ny, k + 1])
        cnt += 1
    return -1

if W==H==1:
    print(0)
else:
    print(bfs())
