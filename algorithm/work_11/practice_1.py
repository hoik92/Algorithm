# 순열 생성
def perm(n, k):
    if n == k:
        print(arr)
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k + 1)
            arr[k], arr[i] = arr[i], arr[k]


def perm2(n, k):
    if k == n:
        print(t)
    else:
        for i in range(n):
            if not visited[i]:
                t[k] = arr[i]
                visited[i] = 1
                perm2(n, k + 1)
                visited[i] = 0


arr = [1, 2, 4, 7, 8, 3]
visited = [0] * len(arr)
t = [0] * len(arr)
perm2(len(arr), 0)
