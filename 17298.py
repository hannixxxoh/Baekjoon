N = int(input())
NGE = list(map(int, input().split()))

answer = [-1]*N
stack = []

for i in range(N):
    while stack and NGE[stack[-1]] < NGE[i]:
        answer[stack.pop()] = NGE[i]
    stack.append(i)
    print(stack, i)


for ans in answer:
    print(ans, end = " ")