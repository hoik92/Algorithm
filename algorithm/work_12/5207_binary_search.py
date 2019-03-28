def binary_search(a):
    global N, M, count
    start, end = 0, N - 1
    l, r = 0, 0
    if n[start] > a:
        return
    if n[end] < a:
        return
    while start <= end:
        mid = (start + end) // 2
        if n[mid] == a:
            count += 1
            return
        elif n[mid] > a:
            end = mid - 1
            if l:
                return
            l, r = 1, 0
        else:
            start = mid + 1
            if r:
                return
            l, r = 0, 1
    return


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    n.sort()

    count = 0
    for i in m:
        binary_search(i)

    print(f"#{tc} {count}")
