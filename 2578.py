import sys
from pprint import pprint

input = sys.stdin.readline

graph = []


def fill(graph, num):
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == num:
                graph[i][j] = 0
                return graph

def check(graph):
    result = 0
    if graph[0][0] + graph[1][1] + graph[2][2] + graph[3][3] + graph[4][4] == 0:
        result += 1
    if graph[0][4] + graph[1][3] + graph[2][2] + graph[3][1] + graph[4][0] == 0:
        result += 1
    for i in range(5):
        if sum(graph[i]) == 0:
            result += 1
        if sum(graph[j][i] for j in range(5)) == 0:  # i번째 열의 합
            result += 1
    if result >= 3:
        return True

for _ in range(5):
    graph.append(list(map(int, input().split())))


seq = 1
for _ in range(5):
    show = list(map(int, input().split()))
    for num in show:
        graph = fill(graph, num)
        if check(graph):
            break
        else:
            seq +=1 

print(seq)