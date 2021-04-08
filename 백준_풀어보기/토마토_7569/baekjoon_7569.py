from collections import deque

temp = list(map(int,input().split()))

# 각각 M=x N=y H=z
M = temp[0]
N = temp[1]
H = temp[2]

box = [[list(map(int, input().split())) for i in range(N)] for _ in range(H)]

visit = [[[0]*M for i in range(N)] for j in range(H)]

queue = deque()

dx = [1,0,0,-1,0,0]
dy = [0,1,0,0,-1,0]
dz = [0,0,1,0,0,-1]

# queue에 정점을 넣어두는 연산
for i in range(M):
    for j in range(N):
        for k in range(H):
            if box[k][j][i] == 1:
                queue.append([k,j,i])

# bfs로 search
def bfs(box, visit, queue):
    # 큐가 돌아갈동안
    while queue:
        # tmp에서 queue의 내용을 뺴준다
        tmp = queue.popleft()
        for i in range(6):
            z = tmp[0] + dz[i]
            y = tmp[1] + dy[i]
            x = tmp[2] + dx[i]
            # 해당 범위 안에 들어갈때
            if(0 <= x < M and 0 <= y < N and 0 <= z < H and box[z][y][x] == 0 and visit[z][y][x] == 0):
                visit[z][y][x] = visit[tmp[0]][tmp[1]][tmp[2]] + 1
                box[z][y][x] = 1
                queue.append([z,y,x])  

bfs(box, visit, queue)

def max_value(box, visit, M, N, H):
    max_value = 0
    for x in range(M):
        for y in range(N):
            for z in range(H):
                # 토마토가 안익었을때
                if box[z][y][x] == 0:
                    return -1
                max_value = max(max_value, visit[z][y][x])

    return max_value

max_data = max_value(box, visit, M, N, H) 

print(max_data)