N = int(input())
NGE = list(map(int, input().split()))

place = [-1]*N
temp = []

for i in range(N):
    while temp and NGE[temp[-1]] < NGE[i]:
        place[temp.pop()] = NGE[i]
    temp.append(i)


for ans in place:
    print(ans, end = " ")