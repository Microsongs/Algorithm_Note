from collections import deque

#점 생성
temp = list(map(int, input().split()))

# 수빈 위치
n = temp[0]
# 동생 위치
k = temp[1]

# 방문 위치
visit = [-1] * 100001
# 방법 갯수
meth = [0] * 100001
loc = n


# bfs
def bfs(visit, meth, start):
    queue = deque()
    queue.append(start)
    result = 0
    # 같은 위치일 경우 예외처리
    if start == k:
        print(visit[k])
        print("0")
        return
    visit[start] = 0
    meth[start] = 1

    while queue:
        tmp = queue.popleft()
        #print(tmp)
        # tmp+1 tmp-1 tmp*2를 한번에 처리
        for i in (tmp+1, tmp-1, tmp*2):
            #범위 내에 들어갈 경우
            if 0 <= i <= 100000:
                # 첫 방문 시
                if visit[i] == -1:
                    visit[i] = visit[tmp] + 1
                    meth[i] = meth[tmp]
                    queue.append(i)
                # 한번 이상 방문시
                elif visit[i] == visit[tmp]+1:
                    meth[i] += meth[tmp]

    print(visit[k])
    print(meth[k])
            

bfs(visit, meth, n)
