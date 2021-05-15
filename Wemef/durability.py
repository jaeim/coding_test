# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, m = map(int, input().split(' '))
grid = [list(map(str, input().split(' '))) for _ in range(n)]

for i in range(n):
    for j in range(n):
        grid[i][j] = int(grid[i][j])

result = []
for i in range(m):
    # idx, a, b = map(int, input().split(' '))
    user_input = list(map(str, input().split(' ')))
    for index, u in enumerate(user_input):
        user_input[index] = int(u)
    if user_input[0] == 1:
        # a = int(input().split(' '))
        a = user_input[1]
        for x in range(n):
            for y in range(n):
                grid[x][y] -= a
                if grid[x][y] < 0:
                    # 아니 미친 여기서 == 을 써서 0으로 안바뀐거였음 ㅎㅎㅎㅎㅎ
                    grid[x][y] = 0
    else:
        # a, b = map(int, input().split(' '))
        a = user_input[1]
        b = user_input[2]
        result.append(grid[a - 1][b - 1])

for i in result:
    print(i)


