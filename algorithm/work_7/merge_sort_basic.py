def merge_sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return merge(left, right)


def merge(left, right):
    len_l, len_r = len(left), len(right)
    result = [0] * (len_l + len_r)
    i, j, k = 0, 0, 0
    while len_l > i and len_r > j:
        if left[i] < right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    while len_l > i:
        result[k] = left[i]
        i += 1
        k += 1
    while len_r > j:
        result[k] = right[j]
        j += 1
        k += 1
    return result

def quick_sort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quick_sort(a, begin, p)
        quick_sort(a, p+1, end)

def partition(a, begin, end):
    pivot = begin
    i = begin
    for j in range(i+1, end):
        if a[pivot] >= a[j]:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[pivot], a[i] = a[i], a[pivot]
    return i

a = [69,10,30,2,16,8,31,22]
print(merge_sort(a))
print(a)
b = [69,10,30,2,16,8,31,22]
quick_sort(b, 0, len(b))
print(b)