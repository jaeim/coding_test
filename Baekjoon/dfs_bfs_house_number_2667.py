
def house_dfs(i, j):
    visited[i][j] = True
    # 해당 단지의 아파트 수
    global house_cnt
    house_cnt += 1
    if i - 1 >= 0:
        if houses[i - 1][j] == 1 and visited[i - 1][j] is False:
            house_dfs(i - 1, j)
    if j - 1 >= 0:
        if houses[i][j - 1] == 1 and visited[i][j - 1] is False:
            house_dfs(i, j - 1)
    if i + 1 < size:
        if houses[i + 1][j] == 1 and visited[i + 1][j] is False:
            house_dfs(i + 1, j)
    if j + 1 < size:
        if houses[i][j + 1] == 1 and visited[i][j + 1] is False:
            house_dfs(i, j + 1)

size = int(input())
houses = [list(map(int, input())) for _ in range(size)]
visited = [[False] * size for _ in range(size)]

# 왜 꼭 이중 for문을 dfs안에서 돌려야 한다고 생각했을까 나는..
# 아파트 단지
cnt = 0
# 아파트 갯수 배열
house_cnt_list = []
# 아파트 갯수
house_cnt = 0
for i in range(size):
    for j in range(size):
        if houses[i][j] == 1 and visited[i][j] is False:
            house_dfs(i, j)
            house_cnt_list.append(house_cnt)
            # 아파트 단지 갯수 초기화
            house_cnt = 0
            # 단지수 카운트
            cnt += 1

house_cnt_list.sort()
print(cnt)
for i in house_cnt_list:
    print(i)

