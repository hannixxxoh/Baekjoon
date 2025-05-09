import sys

input = sys.stdin.readline

string = list(input().rstrip())
exp = input().rstrip()
len_exp = len(exp)
len_string = len(string)


while(True):
    # 다 돌았는데 explode 한번도 안했으면 True
    flag = True

    for idx_s in range(len(string)):
        idx_exp = 0
        
        # string 문자가 exp 첫번째 문자랑 같으면 체크 시작
        if string[idx_s] == exp[idx_exp]:
            idx_check = idx_s
            while(True):
                idx_check += 1

                # string이 None이면 인덱스 + 1
                if string[idx_check] == None:
                    continue

                idx_exp += 1


                if not string[idx_check] == exp[idx_exp]:
                    break
                else:
                    # exp 끝까지 다 일치하면
                    if idx_exp == len_exp - 1:
                        string[idx_s:idx_check + 1] = [None] * (idx_check + 1 - idx_s)
                        flag=False
                        break
    if flag:
        break
        

result = ''.join([s for s in string if bool(s)])
print(result if len(result) > 0 else "FRULA")