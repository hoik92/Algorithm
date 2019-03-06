def merge_sort(A):
    N = len(A)
    if N <= 1:
        return A

    left = merge_sort(A[:N // 2])
    right = merge_sort(A[N // 2:])

    return merge(left, right)

def merge(left, right):
    i, j, k = 0, 0, 0
    result = [0] * (len(left) + len(right))
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    while len(left) > i:
        result[k] = left[i]
        i += 1
        k += 1
    while len(right) > j:
        result[k] = right[j]
        j += 1
        k += 1
    return result

print(merge_sort([6,5,4,3,2,1]))
