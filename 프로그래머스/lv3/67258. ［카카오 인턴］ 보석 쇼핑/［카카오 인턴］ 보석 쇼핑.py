#앞에서 부터 쭉 진행하면서 각 보석의 갯수를 저장해둔다. 하나씩 진행하면서 맨 처음의 보석과 같은 보석이면 맨 처음 인덱스부터 진행하면서 2개 이상인 보석의 갯수를 뺀다.
def solution(gems):
    answer = []
    i = 0
    j = 0
    tu = {}
    type_gems = list(set(gems))
    if len(type_gems) == 1:
        return [1,1]
    for i in type_gems:
        tu[i] = 0
    i = 1
    tu[gems[0]] += 1
    num_1 = 1
    for idx, gem in enumerate(gems[1:]):
        j = idx+2
        tu[gem]+=1
        if tu[gem] == 1:
            num_1 +=1
        if gem == gems[i-1]:
            tmp = i-1
            for k in range(tmp,j):
                if tu[gems[k]] >1:
                    i +=1
                    tu[gems[k]] -=1
                    if tu[gems[k]] == 0:
                        num_1 -=1
                else:
                    break

        if num_1 == len(type_gems):
            answer.append([i, j, j-i])
            
    min = 1000000    
    result = [0,0]
    for ans in answer:
        if ans[2] < min:
            min = ans[2]
            result=[ans[0], ans[1]]
    return result