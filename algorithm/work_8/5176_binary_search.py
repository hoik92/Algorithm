def inorder(t):
    global V
    if t <= N:
        inorder(2 * t)
        V += 1
        value[t] = V
        inorder(2 * t + 1)


for tc in range(1, int(input())+1):
    N = int(input())
    value = [0] * (N + 1)
    V = 0
    inorder(1)
    print("#{} {} {}".format(tc, value[1], value[N // 2]))
