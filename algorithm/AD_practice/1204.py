for tc in range(int(input())):
    t = int(input())
    score = list(map(int, input().split()))
    cnt = [0] * 101
    for i in score:
        cnt[i] += 1
    max_cnt = cnt[0]
    idx = 0
    for i in range(1, len(cnt)):
        if max_cnt <= cnt[i]:
            max_cnt = cnt[i]
            idx = i
    print("#{} {}".format(t, idx))