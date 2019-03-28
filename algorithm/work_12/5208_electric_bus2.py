def backtrack(location, count):
    global N, min_cnt
    if count >= min_cnt:
        return
    if location >= N:
        if count < min_cnt:
            min_cnt = count
        return
    for i in range(m[location], 0, -1):
        backtrack(location + i, count + 1)


for tc in range(1, int(input())+1):
    m = list(map(int, input().split()))
    N = m[0]
    min_cnt = N
    backtrack(1, -1)
    print(f"#{tc} {min_cnt}")
