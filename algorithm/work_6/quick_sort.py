l = [6,5,4,3,2,1]

def quick_sort(l, begin, end):
    if begin < end:
        p = partition(l, begin, end)
        quick_sort(l, begin, p)
        quick_sort(l, p+1, end)

def partition(l, begin, end):
    pivot = begin
    i = begin
    for j in range(i+1, end):
        if l[pivot] >= l[j]:
            i += 1
            l[i], l[j] = l[j], l[i]
            # print(l)
    l[pivot], l[i] = l[i], l[pivot]
    return i

quick_sort(l, 0, len(l))
print(l)