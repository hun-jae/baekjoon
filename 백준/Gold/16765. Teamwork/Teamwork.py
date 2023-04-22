n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
for i in range(k):
    dp[i] = max(arr[:i+1])*(i+1)
for i in range(k, n):
    max_ = arr[i]
    for j in range(k):
        max_ = max(max_, arr[i-j])
        dp[i] = max(dp[i], max_*(j+1) + dp[i-(j+1)])

print(dp[-1])
