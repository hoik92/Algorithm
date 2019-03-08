for tc in range(1, int(input())+1):
    N = int(input())
    m = input().split()
    s = ""
    for i in range(N):
        s += m[i]

    ans = [0] * 2
    ans[0] = int(s[0])
    max_num = 0
    for i in range(1, len(s)):
        if not ans[1]:
            if int(s[i]) >= ans[0]:
                ans[1] = int(s[i])
            else:
                ans[0], ans[1] = int(s[i]), 0
        else:
            if int(s[i]) >= ans[1]:
                ans[0], ans[1] = ans[1], int(s[i])
            else:
                tmp = ans[0] * ans[1]
                if tmp > max_num:
                    max_num = tmp
                ans[0], ans[1] = int(s[i]), 0
    print("#{} {}".format(tc, max_num))