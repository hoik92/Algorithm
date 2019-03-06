"""
세제곱근을 찾아라

양의 정수 N에 대해 N = X^3가 되는 양의 정수X 를 구하여라.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1≤N≤1018) 이 주어진다.

[출력]

각 테스트 케이스마다 첫 번째 줄에는‘#T’(T는 테스트케이스 번호를 의미하며 1부터 시작한다.)를 출력하고, N = X^3가 되는 양의 정수 X를 출력한다.

만약 이런 X가 존재하지 않으면 -1을 출력한다.

입력
3
27
7777
64

출력
#1 3
#2 -1
#3 4
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    U, L = int(N ** 0.4) + 1, int(N ** 0.3)
    result = -1
    # for i in range(L, U+1):
    #     if N // i**2 == i and N % i**2 == 0:
    #         result = i
    #     if result != -1:
    #         break

    mid = (L + U) // 2
    idx = mid
    while idx < U:
        if N // idx**2 == idx and N % idx**2 == 0:
            result = idx
            break
        if N // idx**2 > idx:
            L = mid
        else:
            U = mid
        mid = (L + U) // 2
        if idx == mid:
            break
        else:
            idx = mid

    print(f"#{tc} {result}")