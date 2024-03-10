nums = ["000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"]
alph = ['A','B','C','D','E','F','G','H']
n = int(input())
num = input()
arr = []
answer = ''
for i in range(0, n*6, 6):
    arr.append(num[i:i+6])


def compare(num1, num2):
    numDif = 0
    for i in range(6):
        if num1[i] != num2[i]:
            numDif += 1
    return numDif

for idx, a in enumerate(arr):
    for idx2, b in enumerate(nums):
        if compare(a, b) <= 1:
            answer += alph[idx2]
            break
    else: #만약 겹치는게 없다면
        answer = idx+1
        break
print(answer)

