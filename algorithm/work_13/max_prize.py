def dfs(m, cnt):
    global N, max_prize
    tmp = int(m)
    if cnt == N:
        if tmp > max_prize:
            max_prize = tmp
        return

    if tmp > result[cnt]:
        result[cnt] = tmp
    else:
        return

    m = list(m)
    for i in range(len(m)):
        for j in range(len(m)):
            if i != j:
                m[i], m[j] = m[j], m[i]
                dfs(''.join(m), cnt + 1)
                m[i], m[j] = m[j], m[i]


for tc in range(1, int(input())+1):
    s, N = input().split()
    N = int(N)
    max_prize = 0
    result = [0] * N
    dfs(s, 0)
    print(f"#{tc} {max_prize}")
