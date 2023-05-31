arr = list(map(int, input().split()))
ass = True
des = True
prev = arr[0]
for i in range(1, len(arr)):
    if arr[i] > prev:
        des = False
    else:
        ass = False
    prev = arr[i]
if ass:
    print("ascending")
elif des:
    print("descending")
else:
    print("mixed")
