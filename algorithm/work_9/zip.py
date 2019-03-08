for tc in range(1, int(input())+1):
    N = int(input())
    cnt = 0
    print("#{}".format(tc))
    for i in range(N):
        m = input().split()
        m[1] = int(m[1])
        for j in range(m[1]):
            if cnt == 10:
                print()
                cnt = 0
            cnt += 1
            print(m[0], end='')
    print()