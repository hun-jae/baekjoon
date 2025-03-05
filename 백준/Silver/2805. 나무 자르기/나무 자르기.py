n, m = map(int, input().split())
trees = list(map(int, input().split()))
l, r = 0, max(trees)

while l <= r:
    mid = (l + r) // 2
    total = sum(tree - mid for tree in trees if tree > mid)  # 리스트 내포를 사용하여 총합 계산
    
    if total == m:
        print(mid)
        break
    elif total < m:  # 덜 자른 경우, 높이를 낮춰야 함
        r = mid - 1
    else:  # tree - mid가 m보다 큰 경우
        l = mid + 1
else: 
    print(r)