m = [0] * 50
m[0], m[1], m[2] = 0, 1, 3

def f(n):
    if n > 2 and not m[n]:
        m[n] = f(n-1) + 2 * f(n-2)
    return m[n]

for tc in range(1, int(input())+1):
    N = int(input())
    n = N // 10

    result = f(n)
    print(f"#{tc} {result}")