# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    s = input()
    init = ['0'] * len(s)
    s_list = []
    cnt = 0
    for i in s:
        s_list.append(i)
    
    for i in range(len(s)):
        if init[i] != s_list[i]:
            for j in range(i, len(s)):
                if init[j] == '0':
                    init[j] = '1'
                else:
                    init[j] = '0'
            cnt += 1
    print(f"#{tc} {cnt}")
