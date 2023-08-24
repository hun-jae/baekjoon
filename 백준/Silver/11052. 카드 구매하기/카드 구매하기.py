n = int(input())
arr = list(map(int, input().split()))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j]
        if j >= i:
            dp[i][j] = max(dp[i][j-i] + arr[i-1], dp[i][j])
print(dp[-1][-1])