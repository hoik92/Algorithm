# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    sum_list = []

    for i in range(N - M + 1):
        sum_list.append(sum(N_list[i:i+M]))

    # mx, mn = sum_list[0], sum_list[0]
    # for i in sum_list:
    #     if mx < i:
    #         mx = i
    #     if mn > i:
    #         mn = i

    # print(f"#{tc} {mx-mn}")
    print(f"#{tc} {max(sum_list) - min(sum_list)}")

    

    

    
