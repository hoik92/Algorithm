T = int(input())
for tc in range(1, T+1):
    N = input()
    M = input()
    N_len, M_len = len(N), len(M)

    # for i in range(M_len - N_len + 1):
    #     for j in range(N_len):
    #         if N[j] != M[i+j]:
    #             flag = 0
    #             break
    #         flag = 1
    #     if flag:
    #         break
    #
    # print(f"#{tc} {flag}")

    idx = 0
    while idx <= M_len - N_len:
        flag = 1
        for i in range(N_len - 1, -1, -1):
            if N[i] != M[idx + i]:
                flag = 0
                tmp = M[idx + i]
                for j in range(N_len - 1, -1, -1):
                    if tmp == N[j]:
                        idx += i - j -1
                        break
                idx += 1
                break
        if flag:
            break
    print(f"#{tc} {flag}")