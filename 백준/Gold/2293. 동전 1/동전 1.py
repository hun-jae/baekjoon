n, k = map(int, input().split())
coins = [0]
for i in range(n):
    coins.append(int(input()))
d = [0]*(k+1)
d[0] = 1
for i in range(1, n+1):
    coin = coins[i]
    for j in range(0, k+1):
        if j<coin:
            continue
        else:
            d[j] = d[j] + d[j-coin]
#print(d)
print(d[k])