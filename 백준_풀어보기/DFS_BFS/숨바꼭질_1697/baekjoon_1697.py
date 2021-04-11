from collections import deque

#점 생성
temp = list(map(int, input().split()))

# 수빈 위치
n = temp[0]
# 동생 위치
k = temp[1]

# 방문 위치
visit = [0] * 100001
loc = n
# bfs
def bfs(visit, start):
    queue = deque()
    queue.append(start)
    # 같은 위치일 경우 예외처리
    if start == k:
        return visit[k]
        
    while queue:
        tmp = queue.popleft()
        # +1 처리 -> tmp+1가 0이거나 tmp+1에 tmp보다 방문을 많이 하였을 떄
        if tmp+1 <= 100000 and visit[tmp+1] == 0:
            queue.append(tmp+1)
            visit[tmp+1] = visit[tmp]+1
        # -1 처리
        if tmp-1 >= 0 and visit[tmp-1] == 0:
            queue.append(tmp-1)
            visit[tmp-1] = visit[tmp]+1
        # *2 처리
        if tmp*2 <= 100000 and visit[tmp*2] == 0:
            queue.append(tmp*2)
            visit[tmp*2] = visit[tmp]+1
        # 찼을 경우
        if visit[k] != 0:
            return visit[k]

print(bfs(visit, n))



