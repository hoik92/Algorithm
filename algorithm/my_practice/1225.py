# import sys
# sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    T = input()
    N = list(map(int, input().split()))

    while N[7] != 0:
        for i in range(1, 6):
            tmp = N[0] - i
            for j in range(7):
                N[j] = N[j+1]
            N[7] = tmp
            if N[7] <= 0:
                N[7] = 0
                break

    print(f"#{T}", end=' ')
    for i in N:
        print(i, end=' ')
    print()