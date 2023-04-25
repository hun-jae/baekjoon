from collections import deque
from collections import Counter
import sys
input = sys.stdin.readline
n,k = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(len(input()))

cnt = 0
que = deque()
for i in range(k+1):
    que.append(arr[i])

right = k+1
counter = Counter(que)

while len(que) > 0:
    left = que.popleft()
    counter[left] -= 1
    cnt += counter[left]
    if (right < n):
        que.append(arr[right])
        counter[arr[right]] += 1
        right += 1

print(cnt)