for tc in range(1, int(input())+1):
    N = float(input())

    result = ''
    for i in range(12):
        N = N * 2
        if N >= 1.0:
            result += '1'
            N -= 1.0
        else:
            result += '0'
        if N == 0.0:
            break

    if N != 0.0:
        result = 'overflow'
    print(f"#{tc} {result}")
