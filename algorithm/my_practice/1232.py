def preorder(n):
    if value[n] == '+':
        value[n] = preorder(m[n][0]) + preorder(m[n][1])
    elif value[n] == '-':
        value[n] = preorder(m[n][0]) - preorder(m[n][1])
    elif value[n] == '*':
        value[n] = preorder(m[n][0]) * preorder(m[n][1])
    elif value[n] == '/':
        value[n] = preorder(m[n][0]) // preorder(m[n][1])
    return value[n]

for tc in range(1, 11):
    N = int(input())
    m = [[0] * 2 for _ in range(N + 1)]
    value = [0] * (N + 1)

    for i in range(N):
        tmp = input().split()
        if len(tmp) == 2:
            value[int(tmp[0])] = int(tmp[1])
        else:
            value[int(tmp[0])] = tmp[1]
            m[int(tmp[0])][0] = int(tmp[2])
            m[int(tmp[0])][1] = int(tmp[3])

    result = preorder(1)
    print("#{} {}".format(tc, result))