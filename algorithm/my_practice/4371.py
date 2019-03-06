"""
항구에 들어오는 배

민석이는 항구가 있는 작은 마을에 산다.

이 항구에는 배가 아주 드물게 지나다닌다.

민석이는 어느날 모든 배들이 항구에 들어온 것을 보았다.

민석이는 이 날을 1일차로 지정하였다.

민석이는 배가 한 척이라도 항구에 들렀던 날을 “즐거운 날"로 이름짓고, 1일차부터 즐거운 날들을 모두 기록하였다.

그러던 중, 한 가지 규칙을 발견했는데, 그 규칙은 각 배들은 항구에 주기적으로 들른다는 것이었다.

예를 들어, 주기가 3인 배는 항구에 1일차, 4일차, 7일차, 10일차 등에 방문하게 된다.

민석이가 1일차부터 기록한 “즐거운 날"들의 목록이 주어질 때, 항구에 들렀던 배의 최소 수를 알아내자.

이 때, 항상 답이 존재하는 입력만 주어진다.

[입력]
첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에 즐거운 날의 수 N이 주어진다. (2 ≤ N ≤ 5000)

각 테스트 케이스의 두 번째 줄부터 N개의 줄에 걸쳐 즐거운 날의 정보가 오름차순으로 정렬되어 주어진다.

시작하는 날은 항상 1일이고, 마지막 날은 109보다 작은 값이다.

[출력]
각 테스트 케이스마다 항구에 들렀던 배의 최소 수를 출력한다.

입력
3
3
1
3
4
5
1
7
10
13
19
3
1
500000000
999999999

출력
#1 2
#2 2
#3 1
"""

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    happy = []
    for i in range(N):
        happy.append(int(input()))
    cnt = 0

    # for i in range(1, len(happy)):
    #     if happy[i] != 0:
    #         tmp = happy[i] - happy[0]
    #         cnt += 1
    #         for j in range(1, len(happy)-i):
    #             if happy[i] + tmp*j in happy:
    #                 happy[happy.index(happy[i] + tmp*j)] = 0

    # while len(happy) != 1:
    #     tmp = happy[1] - happy[0]
    #     cnt += 1
    #     for i in range(1, len(happy)):
    #         if happy[0] + tmp*i in happy:
    #             happy.remove(happy[0] + tmp*i)

    # while len(happy) != 1:
    #     cnt += 1
    #     tmp = happy[1] - 1
    #     t = happy[1]
    #     while t in happy:
    #         happy.remove(t)
    #         if not t in happy:
    #             t += tmp

    idx = 1
    r = []
    while N > 1:
        if idx == 1:
            tmp = happy[idx] - 1
            r.append(tmp)
            idx += 1
            cnt += 1
        else:
            tmp = happy[idx] - 1
            flag = 0
            for i in r:
                if tmp % i == 0:
                    flag = 1
                    break
            if flag == 0:
                r.append(tmp)
                cnt += 1
            idx += 1
        N -= 1

    print(f"#{tc} {cnt}")