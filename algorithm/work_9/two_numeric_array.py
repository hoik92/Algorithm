def yaho(X, Y, x, y):
    global maximum
    for i in range(y - x + 1):
        tmp = 0
        for j in range(x):
            tmp += X[j] * Y[i + j]
        if tmp > maximum:
            maximum = tmp

for tc in range(1, int(input())+1):
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    maximum = 0
    if a < b:
        yaho(A, B, a, b)
    else:
        yaho(B, A, b, a)
    print("#{} {}".format(tc, maximum))