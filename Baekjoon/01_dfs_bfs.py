# bfs (선입선출)
from collections import deque
def bfs(graph, visited, start):
    visited[start] = True
    print(start, end=' ')
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] is False:
                visited[i] = True
                print(i, end=' ')
                queue.append(i)

# dfs
def dfs(graph, visited, start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if visited[i] is False:
            dfs(graph, visited, i)

# 입력값을 공백을 기준으로 분리
# split 결과를 int로 변환 => map 함수
n_size, m_size, start = map(int, input().split())
# 방문 여부 저장
visited = []
# 그래프 정보 저장 (0번은 사용x)
graph = [[] for i in range(n_size + 1)]
for i in range(m_size):
    vertex, edge = map(int, input().split())
    # 간선은 양방향
    graph[vertex].append(edge)
    graph[edge].append(vertex)
# ** 정점 오름차순 => 정점의 번호가 낮은 순부터 방문
for i in range(n_size + 1):
    graph[i].sort()
# 0번 idx는 사용안하기 때문
visited = [False] * (n_size + 1)
# print(visited)
# print(graph)

# 결과 출력
dfs(graph, visited, start)
# visited 재 초기화
visited = [False] * (n_size + 1)
print('')
bfs(graph, visited, start)