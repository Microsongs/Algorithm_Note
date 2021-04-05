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

# visit를 초기화
for i in range(computer+1):
    visit.append(False)

linked = 0

#dfs로 구현
def dfs(graph, visit, start):
    visit[start] = True
    
    for i in graph[start]:
        if not visit[i]:
            dfs(graph, visit, i)

dfs(graph, visit, 1)

for i in visit:
    if i == True:
        linked+=1

print(linked-1)