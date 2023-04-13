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
max_ = max(max_, cnt_r)
val = 2 + cnt_r
while cnt_r > 0:
    max_ = max(max_, val)
    cur_cnt = 0
    for l in range(left+1, right+1):
        if arr[l] == "K":
            left = l
            break
        else:
            cur_cnt += 1
    for r in range(right-1, left-1, -1):
        if arr[r] == "K":
            right = r
            break
        else:
            cur_cnt += 1
    cnt_r -= cur_cnt
    val += (2-cur_cnt)
print(max_)