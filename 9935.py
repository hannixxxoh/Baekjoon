import sys
input = sys.stdin.readline

string = input().rstrip()
explosion = input().rstrip()

len_exp = len(explosion)
stack = []


for s in string:
    stack.append(s)
    if ''.join(stack[-len_exp:]) == explosion:

        for _ in range(len_exp):
            stack.pop()


result = ''.join(stack)
print(result if len(result) > 0 else "FRULA")