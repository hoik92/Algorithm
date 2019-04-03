from collections import deque

def BFS():
    global N, M

    while queue:
        n, cnt = queue.popleft()
        if n == M:
            return cnt
        for i in range(4):
            if n < M and cal[i] == 1 and n + 1 <= 1000000 and not m[n + 1]:
                queue.append((n + 1, cnt + 1))
                m[n + 1] = 1
            elif cal[i] == -1 and n - 1 > 0 and not m[n - 1]:
                queue.append((n - 1, cnt + 1))
                m[n - 1] = 1
            elif n < M and cal[i] == 2 and n * 2 <= 1000000 and not m[n * 2]:
                queue.append((n * 2, cnt + 1))
                m[n * 2] = 1
            elif cal[i] == -10 and n - 10 > 0 and not m[n - 10]:
                queue.append((n - 10, cnt + 1))
                m[n - 10] = 1


cal = [1, -1, 2, -10]
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    m = [0] * 1000001
    m[N] = 1
    queue = deque()
    for i in range(4):
        if N < M and cal[i] == 1 and N + 1 <= 1000000:
            queue.append((N + 1, 1))
            m[N + 1] = 1
        elif cal[i] == -1 and N - 1 > 0:
            queue.append((N - 1, 1))
            m[N - 1] = 1
        elif N < M and cal[i] == 2 and N * 2 <= 1000000:
            queue.append((N * 2, 1))
            m[N * 2] = 1
        elif cal[i] == -10 and N - 10 > 0:
            queue.append((N - 10, 1))
            m[N - 10] = 1

    count = BFS()
    print(f"#{tc} {count}")
    del m
