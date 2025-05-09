import sys

input = sys.stdin.readline

k = int(input())
T1 = list(map(int, input().split()))
T2 = list(map(int, input().split()))

def div_and_con(depth, s_t2, e_t2, s_t1, e_t1):
    if depth == k:
        return 1 if T1[s_t1] == T2[s_t2] else 0
    
    mid_t2 = (s_t2 + e_t2) // 2
    mid_t1 = (s_t1 + e_t1) // 2

    orig = div_and_con(depth+1, s_t2, mid_t2, s_t1, mid_t1) + div_and_con(depth+1, mid_t2 + 1, e_t2, mid_t1 + 1, e_t1)
    rev = div_and_con(depth+1, mid_t2 + 1, e_t2, s_t1, mid_t1) + div_and_con(depth+1, s_t2, mid_t2, mid_t1 + 1, e_t1)

    return max(orig, rev)

print(div_and_con(1, 0, 2**(k-1)-1, 0, 2**(k-1)-1))