R, C, N = map(int, input().split())
graph = [list(input()) for _ in range(R)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
#1일때
#짝수는 전체설치
#3, 7, 11일때
# 5, 9, 13일때
if not N % 2: #짝수
    for i in range(R):
        for j in range(C):
            print("O", end="")
        print()
else: #홀수
    if N==1: #0일때 -> 초기 상태
        for line in graph:
            print(*line, sep="")
    else:
        for i in range(R):
            for j in range(C):
                if graph[i][j] == 'O':
                    for d in range(4):
                        ni = i + di[d]
                        nj = j + dj[d]
                        if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] != 'O':
                            graph[ni][nj] = 'X'
        for i in range(R):
            for j in range(C):
                if graph[i][j] != '.':
                    graph[i][j] = '.'
                else:
                    graph[i][j] = 'O'

        if (N-3) % 4 == 0:
            for line in graph:
                print(*line, sep="")

        else:
            for i in range(R):
                for j in range(C):
                    if graph[i][j] == 'O':
                        for d in range(4):
                            ni = i + di[d]
                            nj = j + dj[d]
                            if 0 <= ni < R and 0 <= nj < C and graph[ni][nj] != 'O':
                                graph[ni][nj] = 'X'
            # 이게 5일때
            for i in range(R):
                for j in range(C):
                    if graph[i][j] != '.':
                        graph[i][j] = '.'
                    else:
                        graph[i][j] = 'O'
            for line in graph:
                print(*line, sep="")
