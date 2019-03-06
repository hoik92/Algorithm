import sys
sys.stdin = open('input.txt', 'r')

for _ in range(10):
    tc = int(input())
    ladder = [0] * 100
    for i in range(100):
        ladder[i] = list(map(int, input().split()))

    dx = [-1, 1]

    y = 99
    for j in range(100):
        if ladder[y][j] == 2:
            x = j
            break

    for i in range(100):
        drt = -1
        for j in range(2):
            if 0 < x < 99:
                if ladder[y][x + dx[j]] == 1:
                    drt = j
            elif x == 0:
                if ladder[y][x + dx[1]] == 1:
                    drt = 1
            else:
                if ladder[y][x + dx[0]] == 1:
                    drt = 0
        if drt != -1:
            while ladder[y][x + dx[drt]]:
                x = x + dx[drt]
                if x == 99 or x == 0:
                    break
        y -= 1
    print(f"#{tc} {x}")
