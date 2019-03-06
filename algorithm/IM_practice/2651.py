def DFS(n, time, cnt, s):
    global N, min_time, d, count, number
    if n == N + 1:
        if min_time > time:
            min_time = time
            number = s
            count = cnt
        return
    tmp = 0
    if time >= min_time:
        return
    if n:
        time += t[n - 1]
        cnt += 1
        s += str(n)
    for i in range(n, N + 1):
        tmp += m[i]
        if tmp <= d:
            DFS(i + 1, time, cnt, s)
        else:
            return

d = int(input())
N = int(input())
m = list(map(int, input().split()))
t = list(map(int, input().split()))
min_time = 0
for i in range(N):
    min_time += t[i]

count = 0
number = ""
DFS(0, 0, 0, "")
print(min_time)
print(count)
for i in number:
    print(i, end=' ')
print()