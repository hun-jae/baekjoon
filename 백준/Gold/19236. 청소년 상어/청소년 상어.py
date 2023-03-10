import sys
import copy
sys.setrecursionlimit(1500)

def fish_move(graph):
    for i in range(1,17):
        fish_fin = False
        for x in range(4):
            if fish_fin == True:
                fish_fin=False
                break
            for y, fish in enumerate(graph[x]):
                if fish_fin == True:
                    if x==3:
                        fish_fin=False
                    break
                if fish[0]==i:
                    #print(fish)
                    for _ in range(8):
                        nx = x + dx[fish[1]]
                        ny = y + dy[fish[1]]
                        if nx < 0 or ny < 0 or nx > 3 or ny >3 or graph[nx][ny][0] == -1:
                            if fish[1] == 8:
                                fish[1] = 1
                            else:
                                fish[1] += 1
                        else:
                            tmp = fish
                            graph[x][y] = graph[nx][ny]
                            graph[nx][ny] = tmp
                            fish_fin = True
                            break
    return graph

def shark_move(d, tmp,loc_s, des_s, graph):
    #print(des_s)
    nx = loc_s[0] + d*dx[des_s]
    ny = loc_s[1] + d*dy[des_s]
    #print(graph)
    #print("nx : ", nx, "ny : ", ny)
    if nx< 0 or ny < 0 or nx >3 or ny > 3 or graph[nx][ny][0] == 0:
        #print("stop: ", graph)
        #print("tmp: ", tmp)
        return True, tmp, des_s, loc_s
    else:
        tmp += graph[nx][ny][0]
        des_s = graph[nx][ny][1]
        graph[nx][ny] = [-1, des_s]
        graph[loc_s[0]][loc_s[1]] = [0,0]
        loc_s = [nx,ny]
        #print("go: ",graph)
        #print("tmp: ", tmp)
        return False, tmp, des_s, loc_s

def dfs(sum, max_,loc_s, des_s,graph):
    for i in range(1,4):
        tmp_loc_s = loc_s
        tmp_des_s = des_s
        tmp_sum = sum
        tmp_graph = copy.deepcopy(graph)
        stop, sum, des_s, loc_s = shark_move(i, sum,loc_s, des_s, graph)
        if stop:
            max_ = max(max_, sum)
        else:
            #tmp_graph = fish_move(tmp_graph)
            #print("fish_move: ", tmp_graph)
            graph = fish_move(graph)
            #print("fish_move: ", graph)
            max_ = max(max_, dfs(sum, max_, loc_s,des_s, graph))
        graph = tmp_graph
        loc_s = tmp_loc_s
        des_s = tmp_des_s
        sum = tmp_sum
    return max_

graph = []
for i in range(4):
    tmp = list(map(int, input().split()))
    row = []
    for j in range(4):
        row.append([tmp[j*2],tmp[j*2+1]])
    graph.append(row)
loc_s = [0,0]
des_s = graph[0][0][1]
in_tmp = graph[0][0][0]
graph[0][0] = [-1,des_s] #상어의 위치는 -1
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

graph = fish_move(graph)
max_ = 0
#print(graph)

max_ = dfs(0, max_, loc_s, des_s,graph)
print(max_+in_tmp)