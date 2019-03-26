def binary_search(a, start, end, key):
    if start > end:
        return -1
    mid = (start + end) // 2
    if a[mid] == key:
        return mid
    elif a[mid] > key:
        return binary_search(a, start, mid - 1, key)
    else:
        return binary_search(a, mid + 1, end, key)


a = [1,2,3,4,5,6,7,8]
print(binary_search(a, 0, len(a) - 1, 0))
