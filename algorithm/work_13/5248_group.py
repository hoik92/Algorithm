def make_set(x):
    p[x] = x
    rank[x] = 0


def find_set(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]


def union_set(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if rank[x] < rank[y]:
        p[x] = y
    else:
        p[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    m = list(map(int, input().split()))
    p = [0] * (N + 1)
    rank = [0] * (N + 1)
    result = [0] * (N + 1)
    for i in range(1, N + 1):
        make_set(i)
    for i in range(M):
        union_set(m[2 * i], m[2 * i + 1])
    for i in range(1, N + 1):
        result[find_set(i)] = 1
    print(f"#{tc} {sum(result)}")
