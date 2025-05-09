def solution(citations):
    citations.sort()
    len_citations = len(citations)
    
    start = 0
    end = len_citations - 1
    answer = 0

    while(start<=end):
        mid = (end + start) // 2
        h = citations[mid]
        
        if h <= len_citations - mid:
            start = mid + 1
            answer = h
        else:
            end = mid - 1
    
    return answer

citations = list(map(int, input().rstrip().split()))
print(solution(citations))