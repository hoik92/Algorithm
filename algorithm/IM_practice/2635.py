N = int(input())
cnt = [0] * (N + 1)
result = [[N] for _ in range(N + 1)]
for i in range(1, N + 1):
    result[i].append(i)
    idx = 0
    while result[i][idx] - result[i][idx + 1] >= 0:
        result[i].append(result[i][idx] - result[i][idx + 1])
        idx += 1
    cnt[i] = len(result[i])

max_cnt = 0
for i in range(1, N + 1):
    if cnt[i] > max_cnt:
        max_cnt = cnt[i]
        idx = i
print(max_cnt)
for i in range(max_cnt):
    print(result[idx][i], end=' ')
print()