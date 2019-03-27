def merge_sort(a):
    if len(a) <= 1:
        return a

    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:])

    return merge(left, right)


def merge(left, right):
    l, r = len(left), len(right)
    i, j, k = 0, 0, 0
    result = [0] * (l + r)
    while i < l and j < r:
        if left[i] < right[j]:
            result[k] = right[j]
            j += 1
        else:
            result[k] = left[i]
            i += 1
        k += 1

    while i < l:
        result[k] = left[i]
        i += 1
        k += 1
    while j < r:
        result[k] = right[j]
        j += 1
        k += 1
    return result


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    weight = merge_sort(weight)
    truck = merge_sort(truck)
    # weight.sort(reverse=True)
    # truck.sort(reverse=True)
    max_weight = 0
    i, j = 0, 0
    while i < N and j < M:
        if weight[i] <= truck[j]:
            max_weight += weight[i]
            j += 1
        i += 1
    print(f"#{tc} {max_weight}")
