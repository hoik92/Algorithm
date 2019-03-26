def merge_sort(a):
    if len(a) <= 1:
        return a

    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:])

    return merge(left, right)


def merge(left, right):
    i, j, k = 0, 0, 0
    l, r = len(left), len(right)
    result = [0] * (l + r)
    while i < l and j < r:
        if left[i] > right[j]:
            result[k] = right[j]
            j += 1
        else:
            result[k] = left[i]
            i += 1
        k += 1

    while i < l:
        result[k] = left[i]
        k += 1
        i += 1
    while j < r:
        result[k] = right[j]
        k += 1
        i += 1

    return result

a = [4,3,2,1]
print(merge_sort(a))
