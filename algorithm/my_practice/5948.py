"""
7-3-5 게임

숫자게임을 좋아하는 새샘이는 서로 다른 7개의 정수 중에서 3개의 정수를 골라 합을 구해서 수를 만들려고 한다.

이렇게 만들 수 있는 수 중에서 5번째로 큰 수를 출력하는 프로그램을 작성하라.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 7개의 서로 다른 정수가 공백으로 구분되어 주어진다. 각 정수는 1이상 100이하이다.

[출력]

각 테스트 케이스마다 첫 번째 줄에는 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 답을 출력한다.

입력
2
1 2 3 4 5 6 7
5 24 99 76 1 77 6

출력
#1 14
#2 181
"""

T = int(input())
for tc in range(1, T+1):
    t = list(map(int, input().split()))
    N = len(t)
    result = []

    for i in range(1<<N):
        tmp, cnt = 0, 0
        for j in range(N):
            if i & (1<<j):
                tmp += t[j]
                cnt += 1
        if cnt == 3 and not tmp in result:
            result.append(tmp)

    for x in range(5):
        max_idx = x
        for i in range(x+1, len(result)):
            if result[max_idx] < result[i]:
                max_idx = i
        result[max_idx], result[x] = result[x], result[max_idx]

    print(f"#{tc} {result[4]}")