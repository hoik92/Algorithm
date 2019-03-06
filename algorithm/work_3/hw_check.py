T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    K_list = list(map(int, input().split()))
    check = [0] * N

    for i in K_list:
        check[i-1] += 1

    print(f"#{tc} ", end='')
    for i in range(len(check)):
        if not check[i]:
            print(i+1, end=' ')
    print()