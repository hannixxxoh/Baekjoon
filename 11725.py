from collections import deque

N = int(input())

tree = [None for n in range(N+1)]
graph = [[] for n in range(N+1)]

for n in range(N-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)


queue = deque([])
queue.append(1)

while queue:
    v = queue.popleft()

    for nxt in graph[v]:
        if tree[nxt] == None:
            tree[nxt] = v
            queue.append(nxt)

for t in range(len(tree)):
    if t > 1:
        print(tree[t])
