import sys
sys.setrecursionlimit(10**5)

global ans
global visited

M, N = map(int, sys.stdin.readline().split())
visited = [False]*26
board = []
ans = 0

def dfs(y, x, cmt):
    global ans
    global visited
    ans = max(ans, cmt)
    visited[board[y][x]] = True

    ny = [-1, 1, 0, 0]
    nx = [0, 0, -1, 1]
    for i in range(4):
        dy = y + ny[i]
        dx = x + nx[i]
        if not(0 <= dy < M and 0 <= dx < N):
            continue
        if visited[board[dy][dx]] == False:
            dfs(dy, dx, cmt+1)
            visited[board[dy][dx]] = False

board = [list(map(lambda x: ord(x)-65, list(sys.stdin.readline().strip()))) for m in range(M)]
dfs(0, 0, 1)
print(ans)