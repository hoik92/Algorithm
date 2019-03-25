N = int(input())
min_cnt = N

if N % 5 == 0:
    result = N // 5
else:
    for i in range(N // 5, -1, -1):
        n = N - 5 * i
        if n % 3 == 0:
            result = i + n // 3
            break
        else:
            result = -1
print(result)
