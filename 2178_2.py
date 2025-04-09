from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for n in range(N)]
visited = [[0]*M for n in range(N)]

ny = [1, -1, 0, 0]
nx = [0, 0, 1, -1]

queue = deque([])
queue.append((0, 0))
visited[0][0] = 1

while queue:
    y, x = queue.popleft()
    for i in range(4):
        dy = y + ny[i]
        dx = x + nx[i]

        if not (0 <= dy < N) or not(0 <= dx < M):
            continue

        if visited[dy][dx]==0 and maze[dy][dx]==1:
            visited[dy][dx] = visited[y][x] + 1
            queue.append((dy, dx))

print(visited[N-1][M-1])
