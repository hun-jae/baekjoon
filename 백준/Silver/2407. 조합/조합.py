from fractions import Fraction

n, m = map(int, input().split())
dp = [0 for _ in range(101)]
dp[0] = 1
dp[1] = 1
for i in range(2, 101):
    dp[i] = dp[i-1] * i
print(Fraction(dp[n], (dp[m]*dp[n-m])))