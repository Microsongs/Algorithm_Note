import sys
from collections import deque

# X Y좌표입력
N, M = input().split()
N = int(N)
M = int(M)

#로봇청소기 좌표 r,c 방향d
r, c, d = input().split()
r = int(r)
c = int(c)
d = int(d)

dy = [-1,0,1,0]
dx = [0,1,0,-1]

# 방향 변환
def change(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    else:
        return 2

def back(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    else:
        return 1

maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# d=0 북 d=1 동 d=2 남 d=3 서
def bfs(maps, r, c, d):
    queue = deque()
    maps[r][c] = 2
    queue.append([r,c,d])
    ans = 1

    while queue:
        row, col, di = queue.popleft()
        # 4방향 check
        temp_direction = di

        for i in range(4):
            temp_direction = change(temp_direction)
            new_row,new_col = row+dy[temp_direction], col+dx[temp_direction]

            # a와 b check
            if 0<=new_row<=N and 0<=new_col<=M and maps[new_row][new_col] == 0:
                ans+=1
                maps[new_row][new_col] = 2
                queue.append([new_row,new_col,temp_direction])
                break
            # 이동하지 못할 경우 -> 후진해보고 뒤가 벽이면 종료
            elif i == 3:
                new_row, new_col = row + dy[back(di)], col + dx[back(di)]
                queue.append([new_row, new_col, di])
                # 뒤가 벽이면 종료
                if maps[new_row][new_col] == 1:
                    return ans
    
    return ans

print(bfs(maps,r,c,d))
