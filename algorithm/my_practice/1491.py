# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    N, A, B = map(int, input().split())
    result_list = []
    tmp = []
    for x in range(1, N+1):
        R = x
        C = N // R
        for y in range(1, C+1):
            result = A * abs(R - y) + B * (N - R * y)
            tmp.append(result)
        result_list.append(min(tmp))
        tmp = []
    print(f"#{tc} {min(result_list)}")