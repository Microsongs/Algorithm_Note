computer = int(input())
node = int(input())

graph = []
visit = []

for i in range(computer+1):
    graph.append([])

# 1번 com이 virus에 감염
for i in range(node):
    temp = list(map(int,input().split()))
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

# visit 초기화

# visit를 초기화
for i in range(computer+1):
    visit.append(False)

# bfs
def bfs(graph, visit, start):
    queue = list()
    queue.append(start)
    linked = 0

    # queue가 살아있을 동안
    while queue:
        node = queue.pop(0)
        #방문 완료
        if visit[node] == False:
            visit[node] = True
            for i in graph[node]:
                if visit[i] == False:
                    queue.append(i)

bfs(graph, visit, 1)

linked = 0

for i in visit:
    if i == True:
        linked+=1

print(linked-1)
