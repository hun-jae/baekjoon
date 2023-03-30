INF = int(1e9)
T = int(input())
for tc in range(T):
    # 노드의 개수, 간선의 개수를 입력
    n, m, w = map(int, input().split())
    # 모든 간선에 대한 정보를 담는 리스트 만들기
    edges = []
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [0] * (n + 1)

    # 모든 간선의 정보 입력
    for _ in range(m):
        a, b, c = map(int, input().split())
        # a번 노드에서 b번 노드로 가는 비용이 c라는 의미 (a -> b 의 비용이 c)
        edges.append((a, b, c))
        edges.append((b, a, c))
    for _ in range(w):
        a, b, c = map(int, input().split())
        # a번 노드에서 b번 노드로 가는 비용이 c라는 의미 (a -> b 의 비용이 c)
        edges.append((a, b, -c))

    def bellman_ford(start):
        # 시작 노드에 대해서 초기화
        #distance[start] = 0
        # 전체 m - 1번의 라운드(round)를 반복
        for i in range(n):
            # 매 반복마다 '모든 간선'을 확인한다.
            for j in range((2*m)+w):
                cur_node = edges[j][0]
                next_node = edges[j][1]
                edge_cost = edges[j][2]
                # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                    distance[next_node] = distance[cur_node] + edge_cost
                    # m 라운드에서도 값이 갱신된다면 음수 순환이 존재
                    if i == n - 1:
                        return True
        return False


    # 벨만 포드 알고리즘 수행
    negative_cycle = bellman_ford(1)
    # 음수 순환이 존재하면 YES 출력
    if negative_cycle:
        print("YES")
    else:
        print("NO")
        # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리를 출력
        # for i in range(2, m + 1):
        #     # 도달할 수 없는 경우, -1 출력
        #     if distance[i] == INF:
        #         print("-1")
        #     # 도달할 수 있으면 거리 출력
        #     else:
        #         print(distance[i])