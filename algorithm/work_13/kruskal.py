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


n = 8
m = 11
p = [0] * n
rank = [0] * n
m = [0] * m
m[0] = (12, 1, 7)
m[1] = (28, 1, 4)
m[2] = (67, 1, 2)
m[3] = (17, 1, 5)
m[4] = (24, 2, 4)
m[5] = (62, 2, 5)
m[6] = (20, 3, 5)
m[7] = (37, 3, 6)
m[8] = (13, 4, 7)
m[9] = (45, 5, 6)
m[10] = (73, 5, 7)
m.sort()
print(m)
A = []
for i in range(1, n):
    make_set(i)

idx = 0
result = 0
while idx != len(m):
    if len(A) == n - 2:
        break
    if find_set(m[idx][1]) != find_set(m[idx][2]):
        A.append((m[idx][0], m[idx][1], m[idx][2]))
        result += m[idx][0]
        union_set(m[idx][1], m[idx][2])
    idx += 1
print(A)
print(result)
print(p)
print(rank)
