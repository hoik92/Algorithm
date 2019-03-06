"""
부분집합 합 문제 구현하기
10개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를
계산하는 함수를 작성해보자.
"""

def is_zero(arr):
    n = len(arr)

    for i in range(1, 1 << n):
        result = 0
        for j in range(n):
            if i & (1 << j):
                result += arr[j]
        if result == 0:
            return True
    return False

arr = list(map(int, input().split()))

print(is_zero(arr))