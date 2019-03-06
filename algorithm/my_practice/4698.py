"""
특별한 소수

테네스는 소수를 좋아한다. 소수란 1과 자기 자신만으로 나뉘어 떨어지는 숫자로 작은 것부터 나열하면 2, 3, 5, 7, 11, 13, 17, 19, 23, …같은 수들이 있다.

또한 테네스는 D를 포함하는 숫자도 좋아한다. 그렇기에 소수가 D를 포함하면 더욱 더 좋아하여 특별한 소수라고 부르기로 했다.

예를 들어 D = 3이면 3, 13, 23, … 같은 소수들이 3을 포함하였으므로 테네스는 이런 숫자들을 특별한 소수라고 부를 것이다.

D가 주어질 때, A이상 B이하의 수 중에서 특별한 소수인 것들의 개수를 구하는 프로그램을 작성하라.

[입력]

첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 세 정수 D, A, B(1 ≤ D ≤ 9, 1 ≤ A ≤ B ≤ 106)가 공백으로 구분되어 주어진다.

[출력]

각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별한 소수의 개수를 출력한다.

입력
2
3 10 30
7 1 1000000

출력
#1 2
#2 43506
"""

T = int(input())
prime = [2]
for tc in range(1, T+1):
    D, A, B = map(int, input().split())
    cnt = 0
    if B > prime[-1]:
        for i in range(prime[-1]+1, B+1):
            tmp = 1
            root_i = int(i ** 0.5) + 1
            for j in prime:
                if j > root_i:
                    break
                elif i % j == 0:
                    tmp = 0
                    break
            if tmp == 1:
                prime.append(i)
                # if A <= i and str(D) in str(i):
                #     cnt += 1
    # else:
    for i in prime:
        if i > B:
            break
        elif i >= A and str(D) in str(i):
            cnt += 1
    print(f"#{tc} {cnt}")