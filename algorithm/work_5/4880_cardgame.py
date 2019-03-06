import sys
sys.stdin = open('input4880.txt', 'r')

def merge_sort(A):
    n = len(A)

    if n <= 1:
        return A

    if n % 2:
        slice_len = n // 2 + 1
    else:
        slice_len = n // 2

    left = merge_sort(A[:slice_len])
    right = merge_sort(A[slice_len:])

    return merge(left, right)

def merge(left, right):
    if (left[0][1] == 1 and right[0][1] == 3) or (left[0][1] == 2 and right[0][1] == 1) or (left[0][1] == 3 and right[0][1] == 2) or (left[0][1] == right[0][1]):
        result = left
    else:
        result = right
    return result

for tc in range(1, int(input())+1):
    N = int(input())
    card = list(map(int, input().split()))

    for i in range(N):
        card[i] = (i, card[i])

    result = merge_sort(card)

    print(f"#{tc} {result[0][0] + 1}")