t = int(input())
for tc in range(t):
    n = int(input())
    coins = list(map(int ,input().split()))
    target = int(input())
    dp = [0 for _ in range(target+1)]
    dp[0] = 1
    for coin in coins:
        for i in range(target+1):
            if i < coin: continue
            dp[i] += dp[i-coin]
    print(dp[-1])