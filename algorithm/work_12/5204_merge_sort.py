def merge_sort(a):
    if len(a) <= 1:
        return a

    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:])

    return merge(left, right)


def merge(left, right):
    global count, N
    l, r = len(left), len(right)
    result = [0] * (l + r)

    if left[-1] > right[-1]:
        result[-1] = left[-1]
        count += 1
    else:
        result[-1] = right[-1]
    return result


def quick_sort(a, start, end):
    global N, flag
    if start < end:
        s = partition(a, start, end)
        if flag:
            return
        if s > N // 2:
            quick_sort(a, start, s - 1)
        else:
            quick_sort(a, s + 1, end)


def partition(a, start, end):
    global N, result, flag
    i, j = start, end
    p = a[start]
    while i < j:
        while p >= a[i]:
            i += 1
        while p < a[j]:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]

    a[start], a[j] = a[j], a[start]
    result = a[N // 2]
    if j == N // 2:
        flag = 1
    return j


for tc in range(1, int(input())+1):
    N = int(input())
    a = list(map(int, input().split()))

    count = 0
    flag, result = 0, 0
    merge_sort(a)
    quick_sort(a, 0, N - 1)
    print(f"#{tc} {result} {count}")
