from collections import deque

temp = list(map(int, input().split()))

#F = 총 층수
F = temp[0]
#S = 현재 위치한 층
S = temp[1]
#G = 스타트 링크의 위치
G = temp[2]
#U = 한번에 올라갈 수 있는 층
U = temp[3]
#D = 한번에 내려갈 수 있는 층
D = temp[4]

startLink = [0] * (F+1)
visit = [0] * (F+1)

queue = deque()
# 0~G-1까지
queue.append([S, 0])

# bfs로 search
def bfs(startLink, queue, F, U, D, G):
    while queue:
        #print(startLink)
        tmp, cnt = queue.popleft()
        up_chan = False
        down_chan = False
        # 최대 층 아래일 경우 U만큼 이동
        if tmp+U <= F and startLink[tmp+U] == 0:
            #startLink[tmp+U] = startLink[tmp]+1
            up_chan = True
            queue.append([tmp+U,cnt+1])
        
        # D만큼 내려갔을 때 0보다 클 경우 D만큼 이동
        if 0 < tmp-D and startLink[tmp-D] == 0:
            down_chan = True
            #startLink[tmp-D] = startLink[tmp]+1
            queue.append([tmp-D,cnt+1])
        # 둘 다일때 둘 다 변경
        if up_chan == True and down_chan == True:
            startLink[tmp+U] = cnt + 1
            startLink[tmp-D] = cnt + 1
        elif up_chan == True:
            startLink[tmp+U] = cnt+1
        elif down_chan == True:
            startLink[tmp-D] = cnt+1
        
        # 만약 G에 방문을 하였으면 출력하고 
        if startLink[G] != 0:
            print(startLink[G])
            return
    # queue를 다 돌았어도 이 부분에 오면 방문을 못한 것이므로 use the stairs 출력
    print("use the stairs")

bfs(startLink, queue, F, U, D, G)