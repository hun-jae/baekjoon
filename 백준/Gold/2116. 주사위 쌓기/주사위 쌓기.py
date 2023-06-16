flip = [5, 3, 4, 1, 2, 0]
n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
def cal_max(a, b):
    if a == 6 or b == 6:
        if a == 5 or b == 5:
            return 4
        else:
            return 5
    return 6

max_ = 0

for i in range(6): #1번 주사위의 6면을 밑면으로
    sum_ = 0
    down = dices[0][i] #수를 뜻함
    for j in range(n):
        for idx in range(6):
            if dices[j][idx] == down:
                up = dices[j][flip[idx]] #upidx
                sum_ += cal_max(down, up)
                down = up
                break
    max_ = max(max_, sum_)
print(max_)


