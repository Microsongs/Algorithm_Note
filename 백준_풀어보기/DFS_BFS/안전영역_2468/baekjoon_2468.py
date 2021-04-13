from collections import deque

n = int(input())
# 맵
maps = [list(map(int, input().split())) for i in range(n)]
# 방문한 곳
visit = [[0] * n for i in range(n)]
# 최대 높이
max_height = 0

# 방향 check
dx = [-1,0,1,0]
dy = [0,-1,0,1]

for i in maps:
    tmp = max(i)
    if tmp > max_height:
        max_height = tmp

# 생존할 수 있는 섬의 리스트
max_live = list()

def bfs(start, height):
    queue = deque()
    queue.append(start)
    while queue:
        tmp = queue.popleft()
        for i in range(4):
            x = tmp[0] + dx[i]
            y = tmp[1] + dy[i]
            # 범위 안에 들어갈 경우 and 방문을 안 한경우 and i,j가 height보다 높을 경우
            if 0 <= x < n and 0 <= y < n and visit[x][y] == 0 and maps[x][y] > height:
                visit[x][y] = 1
                queue.append([x,y])
            
# 최대 높이만큼 반복
for _ in range(max_height):
    height = 0
    for i in range(n):
        for j in range(n):
            # 방문을 안했으면서 _보다 클 경우
            if visit[i][j] == 0 and maps[i][j] > _:
                bfs([i,j], _)
                height+=1
    max_live.append(height)
    #print("visit:",visit)
    visit = [[0] * n for i in range(n)]

print(max(max_live))