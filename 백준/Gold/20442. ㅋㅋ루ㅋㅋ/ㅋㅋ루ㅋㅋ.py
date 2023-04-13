#맨왼쪽K와 맨 오른쪽 K 내부에 있는 R의 개수(:=cnt_r)를 세자 (전체 R의 개수도 세야함)
#max_값은 전체 R의 수로 잡고 시작
#처음값을 2 + cnt_r로 잡고 이후 K를 하나씩 좁혀가면서 (+2 - 빠진R의개수)
#left == right 라면 break 하는데 (+1-빠진R의개수)
#left > right 라면 그냥 break
arr = list(input())
left = right = -1
max_ = cnt_r = cnt_r_after_k = 0
for idx, cur in enumerate(arr):
    if cur == "K":
        cnt_r_after_k = 0
        if left == -1:
            left = idx
        right = idx
    else:
        max_ += 1
        if left != -1:
            cnt_r_after_k += 1
            cnt_r += 1
cnt_r -= cnt_r_after_k

if cnt_r == 0:
    print(max_)
    exit(0)

val = 2 + cnt_r
max_ = max(max_, val)
while True:
    if cnt_r <= 0:
        break
    cur_cnt = 0
    for l in range(left+1, right+1):
        if arr[l] == "K":
            left = l
            break
        else:
            cur_cnt += 1

    for l in range(right-1, left-1, -1):
        if arr[l] == "K":
            right = l
            break
        else:
            cur_cnt += 1
    cnt_r -= cur_cnt
    if cnt_r <= 0:
        break

    if left==right:
        val += (1-cur_cnt)
        max_ = max(max_, val)
        break
    elif left > right:
        break
    else:
        val += (2-cur_cnt)
        max_ = max(max_, val)

print(max_)