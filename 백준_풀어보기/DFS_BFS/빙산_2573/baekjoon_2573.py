from collections import deque

# n,m의 배열 생성
n, m = list(map(int, input().split()))

# 지도
maps = [list(map(int, input().split())) for i in range(n)]
# 연산 정보
iceberg = list([0]*m for i in range(n))
visit = list([0]*m for i in range(n))
queue = deque()

dx = [-1, 0, 1 ,0]
dy = [0, -1, 0, 1]

def bfs(start, count):
    queue.append(start)
    melt_queue = deque()
    visit[start[0]][start[1]] = 1
    while queue:
        #4 방향 검증
        tmp = queue.popleft()
        melt_cnt = 0
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            # 범위 안에 들어가면서 옆에 빙하가 없으면서 방문하지 않았을 경우
            """
            if 0<=x<n and 0<=y<m and visit[x][y] == 0:
                if maps[x][y] != 0:
                    queue.append([x,y])
                    visit[x][y] = count
                else:
                    melt_cnt += 1
            """
            if 0<=x<n and 0<=y<m and visit[x][y] == 0 and maps[x][y] != 0:
                queue.append([x,y])
                visit[x][y] = count
            elif 0<=x<n and 0<=y<m and visit[x][y] == 0:
                melt_cnt += 1            
        if melt_cnt:
            melt_queue.append([tmp[0],tmp[1],melt_cnt])
    return melt_queue
# iceberg check
def check(x,y):
    cnt = 0
    for i in range(4):
        # 범위 내에 들어가면서 해당 위치에 빙산이 0일 경우 iceberg값 연산
        if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m and maps[x+dx[i]][y+dy[i]] <= 0:
            cnt += 1
    return cnt

# 년수 
year = 0
count = 1

# 각 칸의 값은 최대 10
while True:
    count = 0

    #bfs로 검증
    for x in range(n):
        for y in range(m):
            if maps[x][y] != 0 and visit[x][y] == 0:
                melts = bfs([x,y], count+1)
                count += 1
                # 녹이기
                while melts:
                    mx, my, cnt = melts.popleft()
                    maps[mx][my] = max(maps[mx][my]-cnt,0)
    if count == 0:
        year = 0
        break
    if count >= 2:
        break

    visit = list([0]*m for i in range(n))
    year += 1

print(year)