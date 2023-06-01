n = int(input())
people = [[-1,-1]]*n
grade = [1] * n
for i in range(n):
    people[i] =list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            grade[i]= grade[i]+1
for i in range(n):
    print(grade[i], end=' ')