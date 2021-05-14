size = int(input())
# 회의 정보
meeting = [[] for _ in range(size)]
for i in range(size):
    start, end = map(int, input().split(" "))
    meeting[i].append(start)
    meeting[i].append(end)
# print(meeting)

## 내가 틀린 이유: 회의 종료시간과 회의 시작시간에 따른 오름차순 정렬을 해야한다!!!! & 시간초과
## 우선 회의 종료시간에 대해 오름차순으로 정렬 후 그 후 시작시간에 대해 오름차순 정렬을 해야한다.
meeting.sort(key=lambda x:(x[1],x[0]))

# 종료시간이 빠른 애들부터 가장 빨리 시작하는 애들을 더해준다.
m_cnt = 0
start = 0
for m in meeting:
    if m[0] >= start:
        m_cnt += 1
        start = m[1]
print(m_cnt)

""" 시간초과 코드 
# 확정된 회의 배열
mt = []
mt_cnt = 0
# 일단 가장 종료시간이 빠른 회의 삽입
mt.append(meeting[0])
mt_cnt += 1
# 실수로 for문 중첩의 순서?를 바꿨다.
# 바깥에 있는 for문에서는 선택된 회의가 for문으로 돌고, 안의 for문에서 회의정보 배열이 돌아야 하는데 이 반대로 했다.
for v in mt:
    v_start = v[0]
    v_end = v[1]
    for m in meeting:
        start = m[0]
        end = m[1]
        if start >= v_end:
            # print("기존 회의 시간 ({0}, {1})".format(v_start, v_end))
            # print("새로운 회의 시간 ({0}, {1})".format(start, end))
            if v_start == v_end:
                # 회의 시작과 종료가 같은 특수한 경우가 존재함. (3, 3)에 (3, 7)이 들어갈 수는 없다.
                if start > v_start:
                    mt.append(m)
                    mt_cnt += 1
                    break
            mt.append(m)
            mt_cnt += 1
            break
# print(mt)
print(mt_cnt)
"""


