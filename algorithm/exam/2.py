def find():
    global max_sum
    for i in range(len(result1)):
        sample = result1.pop()
        for j in range(4):
            for k in range(j + 1, 5):
                for l in range(k + 1, 6):
                    tmp_sum = abs(sample[j] - sample[k]) + abs(sample[k] - sample[l]) + abs(sample[l] - sample[j])
                    if tmp_sum > max_sum:
                        max_sum = tmp_sum


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    m = [0] * N
    for i in range(N):
        m[i] = list(map(int, input().split()))

    result1 = []
    for i in range(N - 1):
        for j in range(M - 2):
            for k in range(j + 1, M - 1):
                result0 = []
                tmp0, tmp1, tmp2 = 0, 0, 0
                for x in range(i + 1):
                    for y in range(j + 1):
                        tmp0 += m[x][y]
                    for y in range(j + 1, k + 1):
                        tmp1 += m[x][y]
                    for y in range(k + 1, M):
                        tmp2 += m[x][y]
                result0.append(tmp0)
                result0.append(tmp1)
                result0.append(tmp2)
                tmp0, tmp1, tmp2 = 0, 0, 0
                for x in range(i + 1, N):
                    for y in range(j + 1):
                        tmp0 += m[x][y]
                    for y in range(j + 1, k + 1):
                        tmp1 += m[x][y]
                    for y in range(k + 1, M):
                        tmp2 += m[x][y]
                result0.append(tmp0)
                result0.append(tmp1)
                result0.append(tmp2)
                result1.append(result0)

    max_sum = 0
    find()
    print(f"#{tc} {max_sum}")
