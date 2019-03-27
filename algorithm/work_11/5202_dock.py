for tc in range(1, int(input())+1):
    N = int(input())
    m = []
    for i in range(N):
        s, e = map(int, input().split())
        if not i:
            m.append((s, e))
        else:
            for j in range(i):
                if e < m[j][1]:
                    m.insert(j, (s, e))
                    break
                if j == i - 1:
                    m.append((s, e))
    count, idx, end = 0, 0, 0
    while idx < N:
        if m[idx][0] >= end:
            count += 1
            end = m[idx][1]
        idx += 1
    print(f"#{tc} {count}")
