def postorder(t):
    if value[t] == '+' or value[t] == '-' or value[t] == '*' or value[t] == '/':
        a = postorder(tree[t][0])
        b = postorder(tree[t][1])
        if value[t] == '+':
            return a + b
        elif value[t] == '-':
            return a - b
        elif value[t] == '*':
            return a * b
        else:
            return a / b
    return int(value[t])

for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 2 for _ in range(N + 1)]
    value = [0] * (N + 1)
    for i in range(N):
        M = input().split()
        m = len(M)
        if m == 4:
            tree[int(M[0])][0] = int(M[2])
            tree[int(M[0])][1] = int(M[3])
        value[int(M[0])] = M[1]

    result = int(postorder(1))
    print("#{} {}".format(tc, result))