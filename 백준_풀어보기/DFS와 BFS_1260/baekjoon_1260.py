input_data = list(map(int, input().split()))

# 정점
dot = input_data[0]
# 간선
line = input_data[1]
# 시작
start = input_data[2]

# 그래프 2차원 리스트로 구현
graph = []

# 빈 그래프를 생성
for i in range(dot+1):
    graph.append([]);

# 그래프 생성
# 딕셔너리 식으로 해당 자리에 input
for i in range(line):
    temp = list(map(int, input().split()))
    # graph.append([temp[0],temp[1]])
    graph[temp[0]].append(temp[1])
    graph[temp[1]].append(temp[0])

for i in range(len(graph)):
    graph[i].sort()

# dfs 함수
def dfs(graph, visit, visited):
    visited[visit] = True
    print(visit, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀 방문
    for i in graph[visit]:
        if not visited[i]:
            dfs(graph, i, visited)
    
visited_dfs = [False] * (dot+1)
# visited_bfs = [False] * (dot+1)

#bfs 함수
def bfs(graph, start):
    visit = list()
    queue = list()

    # 큐에 시작 노드를 넣어줌
    queue.append(start)

    while queue:
        # 맨 앞의 숫자를 뺀다
        node = queue.pop(0)
        if node not in visit:
            print(node, end=' ')
            visit.append(node)
            queue.extend(graph[node])
        

    

dfs(graph, start, visited_dfs)
print()
bfs(graph, start)