from collections import deque
def virus(computers, infected, start):
    infection = 0
    infected[start] = True
    q = deque([start])
    while q:
        v = q.popleft()
        for i in computers[v]:
            if infected[i] is False:
                infected[i] = True
                infection = infection + 1
                q.append(i)
    return infection

num_cmp = int(input())
num_edge = int(input())
# 0번 idx 사용안하므로 컴퓨터갯수 + 1
infected = [False] * (num_cmp + 1)
computers = [[] for i in range(num_cmp + 1)]
for i in range(num_edge):
    v, e = map(int, input().split())
    computers[v].append(e)
    computers[e].append(v)
print(virus(computers, infected, 1))