for tc in range(1, int(input())+1):
    s = input()
    cnt = 0
    result = 0
    for i in s:
        if i == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)
