ans = []
N, M, K = map(int, input().split())
factorial = [1 for _ in range(201)]

for i in range(2,201):
    factorial[i] = factorial[i-1] * i
    
def com(n, r):
    return factorial[n] // (factorial[n-r] * factorial[r])

if K > com(N+M, M):
    print(-1)
    exit(0)
    
for r in range(M-1, 0, -1): 
    cnt_sum = 0
    for n in range(r, N+M):
        if K <= cnt_sum + com(n, r):
            K -= cnt_sum
            ans.append(n)
            break
        else:
            cnt_sum += com(n, r)
ans.append(K-1)
ans_str = ""

for i in range(N+M-1, -1, -1):
    if i in ans:
        ans_str += "z"
    else:
        ans_str += "a"
print(ans_str)