def solution(number, k):
    
    stack = []
    
    for n in number:
        # 스택에 있는 수가 더 작은 경우
        while stack and int(stack[-1]) < int(n) and k>0:
            k-=1
            stack.pop()
        # 스택에 있는 수가 더 큰 경우 / k가 0 이하
        stack.append(n)
        print(n, stack, k)

    if k!= 0:
        stack = stack[:-k]
        
    answer = ''.join(stack)
    return answer

print(solution("41772528419", 4))