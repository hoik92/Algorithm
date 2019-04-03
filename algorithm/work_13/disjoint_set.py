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
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


N = 5
p = [0] * N
rank = [0] * N

for i in range(N):
    make_set(i)
print(p)
print(rank)

union_set(2, 3)
print(p)
print(rank)
union_set(2, 4)
print(p)
print(rank)