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
    result = 0
    # 같은 위치일 경우 예외처리
    if start == k:
        print(visit[k])
        print("1")
        return

    while queue:
        tmp = queue.popleft()
        # +1 처리 -> tmp+1가 0이거나 tmp+1에 tmp보다 방문을 많이 하였을 떄
        if tmp+1 <= 100000 and visit[tmp+1] == 0:
            visit[tmp+1] = visit[tmp]+1
            if k == tmp+1:
                result+=1
                break
            queue.append(tmp+1)


        # -1 처리
        if tmp-1 >= 0 and visit[tmp-1] == 0:
            visit[tmp-1] = visit[tmp]+1
            if k == tmp-1:
                result+=1
                break
            queue.append(tmp-1)


        # *2 처리
        if tmp*2 <= 100000 and visit[tmp*2] == 0:
            visit[tmp*2] = visit[tmp]+1
            if k == tmp*2:
                result+=1
                break
            queue.append(tmp*2)
        """
        # 찼을 경우
        if visit[k] != 0 and (visit[k] < visit[tmp+1] or visit[k] < visit[tmp-1] or visit[k] < visit[tmp*2]):
            break
        """
    # 남은 queue만 비우면서 실행
    while queue:
        tmp = queue.popleft()
        if tmp+1 <= 100000 and k == tmp+1:
            result += 1
        if tmp-1 >= 0 and k == tmp-1:
            result += 1
        if tmp*2 <= 100000 and k == tmp*2:
            result += 1
    print(visit[k])
    print(result)
            

bfs(visit, n)
