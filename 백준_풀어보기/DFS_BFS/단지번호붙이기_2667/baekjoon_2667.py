from collections import deque
n = int(input())

# 2차원 map 생성
town = [list(map(int,list(input()))) for i in range(n)]

visit = [[0]*n for i in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]
# 집 갯수 배열
num = []

# bfs
def bfs(town, visit, sx, sy, order):
    queue = deque()
    visit[sx][sy] = order;
    x, y = sx, sy
    queue.append([x,y])
    result = 0
    # queue가 계속될 동안
    while queue:
        temp = queue.popleft()
        for i in range(4):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            # 범위 안에 들어갈 경우
            if 0 <= x < n and 0 <= y < n:
                # 밟는 곳이 0이면 무시
                if town[x][y] == 0:
                    continue
                # 방문을 하지 않았던 곳일 경우
                elif visit[x][y] == 0:
                    visit[x][y] = order;
                    result+=1
                    queue.append([x,y])
    return result+1

# order = 1부터 시작 -> 1이 마을이므로 햇갈리지 않기 위해서
order = 2

# 순회하며 만날 경우 bfs를 시작
for i in range(n):
    for j in range(n):
        if town[i][j] != 0 and visit[i][j] == 0:
            num.append(bfs(town, visit, i, j, order))
            order+=1

print(len(num))
num.sort()
for i in num:
    print(i)

"""
max_value = 0
for i in range(n):
    max_value = max(max(visit[i]), max_value)

# 집 갯수 출력
print(max_value-1)

num = list(0 for i in range(max_value-1))

for i in range(n):
    for j in range(n):
        if visit[i][j] != 0:
            num[visit[i][j]-2]+=1
        
num.sort()
for i in num:
    print(i)
"""