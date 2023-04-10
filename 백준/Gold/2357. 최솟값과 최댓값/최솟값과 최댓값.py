import math, sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
h = math.ceil(math.log2(n))
tree_size = 1 << (h+1)
tree = [[0, 0] for _ in range(2*tree_size)]


def init(node, start, end):
    if start==end: #리프노드
        tree[node] = [arr[start], arr[start]]
    else:
        left = init(2 * node, start, (start+end)//2)
        right = init(2 * node + 1, (start+end)//2 + 1, end)
        tree[node] = [min(left[0], right[0]), max(left[1], right[1])]
    return tree[node]


def query(node, start, end, left, right):
    if left > end or right < start:
        return [float('inf'), 0]
    if left <= start and end <= right:
        return tree[node]
    le = query(node*2, start, (start+end)//2, left, right)
    r = query(node*2+1, (start+end)//2+1, end, left, right)
    min_ = min(le[0], r[0])
    max_ = max(le[1], r[1])
    return [min_, max_]


init(1, 0, n - 1)
#print(tree)

for i in range(m):
    a, b = map(int, input().split())
    print(*query(1, 0, n-1, a-1, b-1))
    #print(min_, max_)