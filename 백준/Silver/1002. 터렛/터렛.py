import math

tc = int(input())

for _ in range(tc):
    x1, y1, ac, x2, y2, bc = map(int, input().split())
    ab = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    if x1 == x2 and y1 == y2 and ac == bc:
        print(-1)
    elif abs(ac - bc) < ab < ac + bc:
        print(2)
    elif abs(ac - bc) == ab or ac + bc == ab:
        print(1)
    else:
        print(0)