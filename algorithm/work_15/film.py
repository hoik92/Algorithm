def change(depth, seq):
    global D, W, k, cnt
    if depth == k:
        if find():
            cnt = k
        return
    for i in range(seq, D):
        if not changed[i]:
            tmp.append([i, m[i][:]])
            changed[i] = 1
            for j in range(2):
                m[i] = [j] * W
                change(depth + 1, i)
                if cnt >= 0:
                    return
            changed[i] = 0
            idx, origin = tmp.pop()
            m[idx] = origin


def find():
    global D, W, K, what
    count, feat = 0, -1
    for i in range(D):
        if (feat == 0 and m[i][what] == 0) or (feat == 1 and m[i][what] == 1):
            count += 1
        else:
            feat = m[i][what]
            count = 1
        if count >= K:
            break
    if count < K:
        return False
    for i in range(W):
        if i != what:
            count, feat = 0, -1
            for j in range(D):
                if (feat == 0 and m[j][i] == 0) or (feat == 1 and m[j][i] == 1):
                    count += 1
                else:
                    feat = m[j][i]
                    count = 1
                if count >= K:
                    break
            if count < K:
                if not what:
                    what = i
                return False
    return True


for tc in range(1, int(input())+1):
    D, W, K = map(int, input().split())
    m = [0] * D
    for i in range(D):
        m[i] = list(map(int, input().split()))

    changed = [0] * D
    tmp = []
    cnt = -1

    what = 0
    for k in range(K):
        change(0, 0)
        if cnt >= 0:
            break
    if cnt == -1:
        cnt = K
    print(f"#{tc} {cnt}")
