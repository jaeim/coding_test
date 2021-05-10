import sys
# recursion error 때문
sys.setrecursionlimit(10**6)

# 아래 코드는 혼자서 풀려다 약 2시간 동안 엄청난 삽질의 결과..
# def hideAndSeek(N, K, sec):
#         if N == K:
#             return sec
#         # index 0,1,2 == N*2,N+1,N-1
#         list = []
#         list.append(N*2)
#         list.append(N+1)
#         list.append(N-1)
#         # print(list)
#         # 오차값 저장 배열
#         result = [999] * 3
#         # print(result)
#         for i, y in enumerate(list):
#             if y == K:
#                 sec = sec + 1
#                 return hideAndSeek(y, K, sec)
#             elif y > K:
#                 result[i] = y - K
#             else:
#                 tmp = y * 2
#                 if tmp < K:
#                     result[i] = K - tmp
#                 else:
#                     result[i] = tmp - K
#         #  가장 차이가 적은 값을 가진 결과를 N으로 보냄
#         list_idx = result.index(min(result))
#         N = list[list_idx]
#         sec = sec + 1
#         return hideAndSeek(N, K, sec)
from collections import deque
def hideAndSeek(n, k, sec):
    # sec 관리를 잘해야한다.
    # 덱에 한번에 2가지 요소를 넣어주기 위해 중괄호를 2번 사용함.
    # 2차원 배열 =>[[5, 0],[10, 1]...]
    queue = deque([[n, sec]])
    while queue:
        v = queue.popleft()
        value = v[0]
        second = v[1]
        # 같은 graph depth에 있는 애들은 같은 second를 갖고 있어야한다.
        if not visited[value]:
            visited[value] = True
            if value == k:
                return second
            if value * 2 <= 100000:
                queue.append([value * 2, second+1])
            if value + 1 <= 100000:
                queue.append([value + 1, second + 1])
            if 0 <= value - 1:
                queue.append([value - 1, second+1])


visited = [False] * 100001
N, K = map(int, input().split())
sec = hideAndSeek(N, K, 0)
print(sec)