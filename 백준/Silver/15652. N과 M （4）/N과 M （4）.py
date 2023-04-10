n, m = map(int, input().split())
result = []
def find(depth, i):
    if depth == m:
        print(*result)
        return
    #뽑고 넘어감
    result.append(i)
    find(depth+1, i)
    result.pop()
    #안뽑고 넘어감
    if i+1 <= n:
        find(depth, i+1)
find(0, 1)