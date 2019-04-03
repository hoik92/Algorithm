def find(idx):
    global result
    if sum(tmp) < result:
        result = sum(tmp)
    if idx > 11:
        return
    for i in range(idx, 12):
        a, b, c = 0, 0, 0
        if sum(tmp[i:i + 3]) > fee[2]:
            a = tmp[i]
            tmp[i] = fee[2]
            if i < 11:
                b = tmp[i + 1]
                tmp[i + 1] = 0
            if i < 10:
                c = tmp[i + 2]
                tmp[i + 2] = 0
            find(i + 3)
            tmp[i] = a
            if i < 11:
                tmp[i + 1] = b
            if i < 10:
                tmp[i + 2] = c


for tc in range(1, int(input())+1):
    fee = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    tmp = [0] * 12

    result = fee[3]
    for i in range(12):
        if plan[i]:
            if fee[0] * plan[i] > fee[1]:
                tmp[i] = fee[1]
            else:
                tmp[i] = fee[0] * plan[i]
    if result > sum(tmp):
        result = sum(tmp)
    find(0)
    print(f"#{tc} {result}")
