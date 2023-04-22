n, m = map(int, input().split())
m_arr = list(map(int, input().split()))
c_arr = list(map(int, input().split()))
mc_arr = [[c_arr[i], m_arr[i]] for i in range(len(m_arr))]
mc_arr.sort()
dp = [[0 for _ in range(sum(c_arr)+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(sum(c_arr) + 1):
        if mc_arr[i-1][0] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-mc_arr[i-1][0]] + mc_arr[i-1][1])

for j in range(sum(c_arr)+1):
    for i in range(1, n+1):
        if dp[i][j] >= m:
            print(j)
            exit(0)