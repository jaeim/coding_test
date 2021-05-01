''' DFS '''
# 스택(list) 또는 재귀함수를 사용
# v : 시작점
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    # graph[v] : v에 연결된 정점들
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

''' BFS '''
# 큐 사용
from collections import deque


def bfs(graph, start, visited):
    # 큐 구현 (큐에 방문한 노드들은 삽입, 삭제하며 visited를 갱신)
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                # 뒤로 차례대로 삽입 like list, 대신 맨 왼쪽부터 나감
                queue.append(i)
                visited[i] = True



# 그래프 정보 (2차원 리스트)
# 그래프의 0번 인덱스는 비워둔다. 보통 문제에서 1번 노드부터 시작하는 경우가 많기 때문
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * len(graph)

# dfs(graph, 1, visited)
bfs(graph, 1, visited)