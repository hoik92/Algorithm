def find_pal(N_list):
    result = 0
    for i in range(N):
        for j in range(N - M + 1):
            if N_list[i][j:j + M] == N_list[i][j:j + M][::-1]:
                result = ''.join(N_list[i][j:j + M])
                break
        if result:
            break
    return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = [0] * N
    for i in range(N):
        N_list[i] = list(input())

    result = find_pal(N_list)

    if not result:
        for i in range(N):
            for j in range(N):
                if i < j:
                    N_list[i][j], N_list[j][i] = N_list[j][i], N_list[i][j]
        result = find_pal(N_list)

    print(f"#{tc} {result}")