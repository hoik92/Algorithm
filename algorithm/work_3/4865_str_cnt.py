T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    cnt = [0] * N

    for i in range(M):
        for j in range(N):
            if str2[i] == str1[j]:
                cnt[j] += 1

    cnt_max = cnt[0]
    for i in range(1, N):
        if cnt_max < cnt[i]:
            cnt_max = cnt[i]

    print(f"#{tc} {cnt_max}")