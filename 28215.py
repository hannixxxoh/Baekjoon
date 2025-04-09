import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())

house_lst = []

for _ in range(N):
    x, y = map(int, input().split())
    house_lst.append([x, y])

comb = combinations(house_lst, K)

INF = float("INF")
result = INF
for c in comb:

    # 현재 조합의 가장 최대 거리
    distance = 0
    for house in house_lst:
        distance_house = INF
        # 모든 shelter를 다 돌면서 가장 짧은거리 저장
        for shelter in c:
            distance_now = abs(house[0] - shelter[0]) + abs(house[1] - shelter[1])
            distance_house = min(distance_house, distance_now)
        distance = max(distance, distance_house)
    result = min(result, distance)

print(result)
    