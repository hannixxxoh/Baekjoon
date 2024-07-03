from collections import deque

N, M = map(int, input().split())
field = [list(map(int, input())) for n in range(N)]
visited = [[0]*M for n in range(N)]

queue = deque([])
queue.append((0,0))
visited[0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    y, x = queue.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not(0 <= ny < N) or not(0 <= nx < M):
            continue
        if visited[ny][nx] == 0 and field[y][x] == 1:
            visited[ny][nx] = visited[y][x] + 1
            queue.append((ny, nx))

print(visited[N-1][M-1])

[[1, 1, 4, 4], [2, 2, 5, 5], [3, 3, 7, 8]], 1, 1, 5, 3