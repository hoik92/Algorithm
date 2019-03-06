# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    a = input()
    N_list = [0] * N
    N_count = [0] * 10
    for i in range(N):
        N_list[i] = int(a[i])
        N_count[N_list[i]] += 1

    count = max(N_count)
    for i in range(9, -1, -1):
        if N_count[i] == count:
            index = i
            break
            
    print(f"#{tc} {index} {count}")
    