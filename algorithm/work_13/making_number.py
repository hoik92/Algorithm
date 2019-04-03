def find(n, depth):
    global N, min_val, max_val
    if depth == N:
        if n < min_val:
            min_val = n
        if n > max_val:
            max_val = n
        return

    for i in range(4):
        if cal[i]:
            cal[i] -= 1
            if i == 0:
                find(n + number[depth], depth + 1)
            elif i == 1:
                find(n - number[depth], depth + 1)
            elif i == 2:
                find(n * number[depth], depth + 1)
            else:
                find(int(n / number[depth]), depth + 1)
            cal[i] += 1


for tc in range(1, int(input())+1):
    N = int(input())
    cal = list(map(int, input().split()))
    number = list(map(int, input().split()))

    min_val = 9 ** N
    max_val = -(9 ** N)
    find(number[0], 1)
    print(f"#{tc} {max_val - min_val}")
