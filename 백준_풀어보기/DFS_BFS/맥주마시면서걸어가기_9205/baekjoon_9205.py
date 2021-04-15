from collections import deque
import math

t = int(input())

dx = [0,-1000,0,1000]
dy = [-1000,0,1000,0]

# dfs
def bfs(start, convini, festival):
    queue = deque()
    visit = list()
    queue.append(start)
    visit.append(start)
    while queue:
        tmp = queue.popleft()
        for i in convini:
            # 멘헤튼 거리가 1000 이하이면 이동 가능
            if abs(tmp[0] - i[0]) + abs(tmp[1]-i[1]) <= 1000 and i not in visit:
                queue.append(i)
                visit.append(i)
        if abs(tmp[0] - festival[0]) + abs(tmp[1]-festival[1]) <= 1000:
            visit.append(festival)
            break
    #print (visit)
    if festival in visit:
        print("happy")
    else:
        print("sad")

# test case만큼 실행
for _ in range(t):
    # convination 편의점
    convini = list()
    # 편의점 개수
    tmp = int(input())
    # 내 위치
    me_x, me_y = list(map(int, input().split()))
    # 편의점 좌표
    for i in range(tmp):
        convini.append(list(map(int, input().split())))

    #festival 좌표
    festival = list(map(int,input().split()))

    bfs([me_x, me_y], convini, festival)