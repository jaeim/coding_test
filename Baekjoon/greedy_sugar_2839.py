
# 아래는 내가 스스로 푼 내용인데..뭔가 비효율적이다..
# 애초에 그리디 유형이었는데 왜 모든 유형을 다 구했을까 나는..?
def sugar_myself(n, sugarList):
    cnt_3 = int(n / sugarList[0])
    result = []
    # cnt_3이 2이면 0,1,2를 따져봐야함.
    for i in range(cnt_3 + 1):
        # 계산하고 남은 설탕 계산
        tmp = n - (sugarList[0] * i)
        if tmp == 0:
            result.append(i)
        elif tmp < sugarList[1]:
            result.append(-1)
        else:
            # 5kg의 갯수
            j = int(tmp / sugarList[1])
            tmp = tmp % (sugarList[1] * j)
            if tmp == 0:
                result.append(i+j)
            else:
                result.append(-1)
    # print(result)
    min = 99999
    for i in result:
        if i > 0 and i < min:
            min = i
    # 모든 결과가 다 -1일 경우(정확하게 Nkg을 만족시킬 수 없는 경우)
    if min == 99999:
        min = -1
    print(min)

# 그리디 방식 (인터넷참고)
def sugar_greedy(n):
    cnt = 0
    while True:
    # n이 5의 배수가 될때까지 n-3을 해준다.
        if (n % 5) == 0:
            cnt = cnt + int(n / 5)
            print(cnt)
            break
        n -= 3
        cnt += 1
        if n == 0:
            print(cnt)
            break
        if n < 3:
            print(-1)
            break


# sugarList = [3, 5]
n = int(input())
# sugar_myself(n, sugarList)
sugar_greedy(n)
