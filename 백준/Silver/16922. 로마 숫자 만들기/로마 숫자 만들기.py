n=int(input())
nums=[]
numList = [1,5,10,50]
def search(depth, num, start):
    if depth==n:
        nums.append(num)
        return
    for i in range(start, 4):
        search(depth+1, num+numList[i], i)
search(0,0,0)
print(len(set(nums)))