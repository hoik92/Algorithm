for tc in range(1, 11):
    N = int(input())
    result = 1
    for i in range(N):
        tmp = input().split()
        if result:
            if len(tmp) == 4 and tmp[1] != '+' and tmp[1] != '-' and tmp[1] != '*' and tmp[1] != '/':
                result = 0
            elif len(tmp) == 2 and (tmp[1] == '+' or tmp[1] == '-' or tmp[1] == '*' or tmp[1] == '/'):
                result = 0
    print("#{} {}".format(tc, result))
