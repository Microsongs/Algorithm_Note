from collections import deque

temp = list(map(int,input().split()))
# x축
n = temp[0]
# y축
m = temp[1]

# x축과 y축 check
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 미로 리스트 생성
maze = [list(map(int, list(input()))) for _ in range(n)]

# visit 리스트 생성
visit = [[0]*m for i in range(n)]

# bfs로 서치
def bfs(maze, visit, start):
    queue = deque()
    visit[0][0] = 1
    x,y = 0, 0
    queue.append([x,y])

    while queue:
        Q = queue.popleft()
        for i in range(4):
            x = Q[0] + dx[i]
            y = Q[1] + dy[i]
            # 그래프 내 범위일 경우
            if(0 <= x < n and 0 <= y < m):
                # 밟는 곳이 0이면 무시
                if(maze[x][y] == 0):
                    continue
                # visit[x,y]가 0일 경우 +1
                if(visit[x][y] == 0):
                    visit[x][y] = visit[Q[0]][Q[1]] + 1
                    queue.append([x,y])
    print(visit[n-1][m-1])
                

bfs(maze, visit, 1);