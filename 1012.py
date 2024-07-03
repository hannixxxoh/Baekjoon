import sys

sys.setrecursionlimit(10000)

def dfs(y, x):
    dy = (-1, 1, 0, 0)
    dx = (0, 0, -1, 1)
    field[y][x] = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if not(0 <= ny < N and 0 <= nx < M):
            continue
        if field[ny][nx] == 0:
            continue
        if field[ny][nx] == 1:
            dfs(ny, nx)

T = int(input())
answer = []
for t in range(T):
    ans = 0
    # 인접행렬 생성
    M, N, K= list(map(int, input().split())) # M: 열 N: 행
    field = [[0]*M for _ in range(N)]
    for k in range(K):
        x, y = list(map(int, input().split()))
        field[y][x] = 1
    # dfs 계산
    for x in range(M):
        for y in range(N):
            if field[y][x] == 1:
                # for a in range(N):
                #     print(field[a])
                # print()
                ans += 1
                dfs(y, x)
    answer.append(ans)

for ans in answer:
    print(ans)