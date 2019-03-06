for tc in range(1, int(input())+1):
    N = int(input())
    m = list(map(int, input().split()))
    tree = [0] * (N + 1)

    for i in range(1, N + 1):
        tree[i] = m[i - 1]
        n = i
        while n // 2 != 0:
            if tree[n] < tree[n // 2]:
                tree[n], tree[n // 2] = tree[n // 2], tree[n]
            n = n // 2

    result = 0
    n = N // 2
    while n != 0:
        result += tree[n]
        n = n // 2
    print("#{} {}".format(tc, result))