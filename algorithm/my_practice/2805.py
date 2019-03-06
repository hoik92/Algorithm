# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    N_list, tmp = [], []
    for i in range(N):
        s = input()
        for j in s:
            tmp.append(j)
        N_list.append(list(map(int, tmp)))
        tmp = []
    
    value = 0
    for i in range(N//2):
        value += sum(N_list[i][N//2 - i:N//2 + 1+i])
        value += sum(N_list[N-1-i][N//2 - i:N//2 + 1+i])
    value += sum(N_list[N//2][:])
    print(f"#{tc} {value}")