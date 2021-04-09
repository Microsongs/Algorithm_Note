node = int(input())
temp = list(map(int, input().split()))

# 시작과 끝 노드
start = temp[0]
end = temp[1]

num = int(input())

graph = []
visit = []

for i in range(node+1):
    graph.append([])
    visit.append(0)

# 그래프에 노드 삽입
for i in range(num):
    temp = list(map(int, input().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

# 정렬
for i in range(node):
    graph[i].sort()

# bfs
def bfs(graph, visit, start):
    queue = list()
    queue.append(start)
    while queue:
        tmp = queue.pop(0)
        # pop한것이 tmp가 0일 경우
        for i in graph[tmp]:
            if(visit[i] == 0):
                visit[i] = visit[tmp]+1
                queue.append(i)

bfs(graph, visit, start)

if visit[end] != 0:
    print(visit[end])
else:
    print("-1")