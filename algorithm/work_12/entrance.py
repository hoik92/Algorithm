def binary_search():
    global N, M, max_time
    start, end = 0, max_time
    while start < end:
        count = 0
        mid = (start + end) // 2
        for i in range(N):
            count += mid // n[i]
        if end - start == 1:
            return end
        if count >= M:
            end = mid
        else:
            start = mid
    return end


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    n = [0] * N
    for i in range(N):
        n[i] = int(input())

    result = 0
    max_time = max(n) * M
    result = binary_search()
    print(f"#{tc} {result}")
