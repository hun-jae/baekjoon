dr = [0, -1, -1]
dc = [-1, 0, -1]
dt = [[0, 2], [1, 2], [0, 1, 2]]
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][1] = [1, 0, 0]
for r in range(N):
    for c in range(2, N):
        if graph[r][c] == 1: continue
        for d in range(3): #가로 세로 대각선
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N:
                if d==2:
                    if graph[r-1][c] == 1 or graph[r][c-1] == 1:
                        continue
                    dp[r][c][d] = dp[nr][nc][dt[d][0]] + dp[nr][nc][dt[d][1]] + dp[nr][nc][dt[d][2]]
                else:
                    dp[r][c][d] = dp[nr][nc][dt[d][0]] + dp[nr][nc][dt[d][1]]

print(sum(dp[N-1][N-1]))