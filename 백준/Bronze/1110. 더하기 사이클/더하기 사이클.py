x = int(input())
x_left = int(x/10)
x_right = int(x%10)
new_x = (x_left + x_right)%10 + x_right*10
new_x_left = int(new_x / 10)
new_x_right = int(new_x % 10)
cnt=1
while x != new_x:
    new_x = (new_x_left + new_x_right)%10 +new_x_right*10
    new_x_left = int(new_x / 10)
    new_x_right = int(new_x % 10)
    cnt+=1
print(cnt)

