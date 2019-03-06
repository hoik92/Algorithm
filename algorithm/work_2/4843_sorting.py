# import sys
# sys.stdin = open('input.txt', 'r')

def sorting(A):
    for i in range(10):
        idx = i
        for j in range(i, N):
            if (10-i) % 2:
                if A[idx] > A[j]:
                    idx = j
            else:
                if A[idx] < A[j]:
                    idx = j
        A[i], A[idx] = A[idx], A[i]
    return A

for tc in range(1, int(input())+1):
    N = int(input())
    A = list(map(int, input().split()))
    
    A = sorting(A)

    print(f"#{tc}", end=' ')
    for i in range(10):
        print(A[i], end=' ')
    print()