for tc in range(1, int(input())+1):
    L, U, X = map(int, input().split())
    if L <= X <= U:
        result = 0
    elif X < L:
        result = L - X
    else:
        result = -1
    print(f"#{tc} {result}")