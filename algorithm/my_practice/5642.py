def find_max(n):
    global max_val, N
    tmp = value[n - 1] + m[n - 1]
    value[n] = tmp
    if tmp > max_val:
        max_val = tmp
    for i in range(n, N):
        tmp -= m[i - n]
        tmp += m[i]
        if tmp > max_val:
            max_val = tmp


for tc in range(1, int(input())+1):
    N = int(input())
    m = list(map(int, input().split()))
    max_val = max(m)
    value = [0] * (N + 1)
    value[1] = m[0]
    for i in range(2, N + 1):
        find_max(i)
    print("#{} {}".format(tc, max_val))
